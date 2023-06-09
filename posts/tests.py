from django.test import TestCase
from .models import User, Post, Comment
from django.urls import reverse, resolve
from . import views

# test create post
class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_create_post(self):
        post = Post.objects.create(user=self.user, title='Test Post', body='<p>This is a test post</p>')
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.user, self.user)
        self.assertEqual(post.body, '<p>This is a test post</p>')
        self.assertIsNotNone(post.created_at)

# test new comment
class CommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(user=self.user, title='Test Post', body='<p>This is a test post</p>')

    def test_create_comment(self):
        comment = Comment.objects.create(post=self.post, body='Test comment')
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.body, 'Test comment')
        self.assertIsNotNone(comment.created)

# list all posts for registered user
class PostTestCase2(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post1 = Post.objects.create(user=self.user, title='Test Post 1', body='<p>This is test post 1</p>')
        self.post2 = Post.objects.create(user=self.user, title='Test Post 2', body='<p>This is test post 2</p>')

    def test_get_user_posts(self):
        posts = Post.objects.filter(user=self.user)
        self.assertEqual(posts.count(), 2)
        self.assertIn(self.post1, posts)
        self.assertIn(self.post2, posts)

# post delete unit testing
class DeletePostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.post = Post.objects.create(user=self.user, title='Test Post', body='<p>This is a test post</p>')

    def test_delete_post(self):
        post_count = Post.objects.count()
        self.post.delete()
        self.assertEqual(Post.objects.count(), post_count - 1)

# endpoints testing
class UrlsTestCase(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_post_url(self):
        url = reverse('post', args=['test-id'])
        self.assertEqual(resolve(url).func, views.post)
        self.assertEqual(resolve(url).kwargs['id'], 'test-id')

    def test_create_post_url(self):
        url = reverse('create_post')
        self.assertEqual(resolve(url).func, views.create_post)

    def test_login_view_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login_view)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_logout_view_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout_view)

    def test_create_comment_url(self):
        url = reverse('create_comment')
        self.assertEqual(resolve(url).func, views.create_comment)