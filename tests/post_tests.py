from django.test import TransactionTestCase

from apps.posts.models import Post
from apps.posts.models.factory import PostFactory


class PostModelTestCase(TransactionTestCase):
    def test_estimate_reading_time(self):
        post = PostFactory(content="")
        self.assertEqual(post.estimate_reading_time, 0)

        post = PostFactory(content="test" * 500)
        self.assertEqual(post.estimate_reading_time, 4)

    def test_title(self):
        post = PostFactory()
        self.assertEqual(post.title, str(post))

    def test_status(self):
        public_posts = [
            PostFactory(status=Post.Status.PUBLISHED),
            PostFactory(status=Post.Status.ONLY_LINK),
        ]
        private_posts = [
            PostFactory(status=Post.Status.DRAFT),
            PostFactory(status=Post.Status.PRIVATE),
        ]

        posts = list(Post.objects.public())

        self.assertCountEqual(public_posts, list(posts))
        self.assertNotIn(private_posts, list(posts))

        posts = list(Post.objects.public_on_category())

        self.assertTrue(
            all([post.status == Post.Status.PUBLISHED for post in posts])
        )

    def test_get_absolute_url(self):
        post = PostFactory()
        self.assertEqual(post.get_absolute_url(), f"/posts/{post.slug}/")

        page = PostFactory(is_page=True)
        self.assertEqual(page.get_absolute_url(), f"/pages/{page.slug}/")
