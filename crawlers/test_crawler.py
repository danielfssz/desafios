import unittest
from crawler import getData, returnInfos
import codecs

mock_html=codecs.open("mock_html.html", 'r')
invalid_mock_html=codecs.open("invalid_mock_html.html", "r")

class testCrawler(unittest.TestCase):
    def test_return_right_infos(self):
        mock_response = """[{'erro': '', 'votos': '78951', 'subreddit': 'worldnews', 'titulo': "'Anti-vax news (sbs.com.au)", 'link_comentarios': 'https://old.reddit.com/r/worldnews/comments/a21lfl/antivax_movement_blamed_for_30_per_cent_jump_in/', 'link_thread': 'https://www.sbs.com.au/news/anti-vax-movement-blamed-for-30-per-cent-jump-in-measles-cases-worldwide'}, {'erro': '', 'votos': '37320', 'subreddit': 'worldnews', 'titulo': 'RussiaCanada news (cbc.ca)', 'link_comentarios': 'https://old.reddit.com/r/worldnews/comments/a1yibb/canada_leads_joint_g7_statement_condemning/', 'link_thread': 'https://www.cbc.ca/news/politics/canada-russia-ukraine-g7-1.4927879'}, {'erro': '', 'votos': '6018', 'subreddit': 'worldnews', 'titulo': 'Peru news (telesurenglish.net)', 'link_comentarios': 'https://old.reddit.com/r/worldnews/comments/a1tgh2/peru_8000_barrels_of_oil_spill_into_amazon_after/', 'link_thread': 'https://www.telesurenglish.net/news/Peruvian-Official-Accuses-Indigenous-Mayuriaga-of-Spilling-8000-Barrels-of-Oil-in-Amazon-20181129-0001.html'}]"""

        thread = 'worldnews'
        source = mock_html
        result = getData(thread, source)
        
        self.assertEqual(str(result), mock_response)

    def test_return_message_when_thread_is_invalid(self):
        thread = 'huehuehuehue'
        source = invalid_mock_html
        result = getData(thread, source)

        self.assertEqual(result[0]['erro'], "huehuehuehue não é uma thread válida!")

    def test_list_of_threads_is_not_empty(self):
        threads = ''

        with self.assertRaises(ValueError):
            returnInfos(threads)

    def test_if_there_is_an_invalid_character_in_thread(self):
        threads = 'asdasda@adasd;usa'

        with self.assertRaises(ValueError):
            returnInfos(threads)