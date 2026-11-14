import unittest

from echo360.videos import EchoCloudVideo


class FeedSelectionTest(unittest.TestCase):
    def make_video(self, alternative_feeds=False, second_feed=False):
        # build a bare EchoCloudVideo without running the network-driven __init__
        video = object.__new__(EchoCloudVideo)
        video.download_alternative_feeds = alternative_feeds
        video.download_second_feed_only = second_feed
        return video

    def test_default_downloads_first_feed_only(self):
        video = self.make_video()
        urls = ["feed1.m3u8", "feed2.m3u8"]
        self.assertEqual(video._select_feed_urls(urls), ["feed1.m3u8"])

    def test_alternative_feeds_downloads_both(self):
        video = self.make_video(alternative_feeds=True)
        urls = ["feed1.m3u8", "feed2.m3u8"]
        self.assertEqual(video._select_feed_urls(urls), urls)

    def test_second_feed_only_skips_first(self):
        video = self.make_video(second_feed=True)
        urls = ["feed1.m3u8", "feed2.m3u8"]
        self.assertEqual(video._select_feed_urls(urls), ["feed2.m3u8"])

    def test_second_feed_only_with_single_feed(self):
        video = self.make_video(second_feed=True)
        self.assertEqual(video._select_feed_urls(["only.m3u8"]), [])

    def test_single_string_url_wrapped_in_list(self):
        video = self.make_video()
        self.assertEqual(video._select_feed_urls("single.m3u8"), ["single.m3u8"])


if __name__ == "__main__":
    unittest.main()
