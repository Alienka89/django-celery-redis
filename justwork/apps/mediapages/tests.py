from django.test import TestCase
from django.urls.base import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import (Page, Block)
import random


class LittleTestClass(APITestCase,TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def _create_block(self, page_id):
        rand = random.randint(1, 100)
        Block.objects.create(
            page_id=page_id,
            title='Test title' + str(rand),
            order_number=random.randint(1, 100),
            text='Test text',
            audio='course-audio.ogg',
            bitrate='300',
            video='https://www.youtube.com/watch?v=XOpDIGgePCM',
            video_sub=''
        )

    def _create_page(self):
        rand = random.randint(1, 100)
        page = Page.objects.create(
            order_number=rand,
            title="Test title " + str(rand)
        )
        for i in range(5):
            self._create_block(page.id)
        return page

    def test_create_page(self):
        page = self._create_page()
        self.assertTrue(len(page.title) > 0)
        self.assertEqual(len(page.block.values('id')), 5)

    def test_get_page(self):
        page = self._create_page()
        urls = ['http://127.0.0.1:8000/api/mediapages/',
               'http://127.0.0.1:8000/api/mediapages/'+str(page.id)+'/']

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
