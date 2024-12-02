import unittest
import sys
import os

# 프로젝트 루트를 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from expense_manager_library.data_cleaner import categorize

class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        # 테스트용 데이터
        self.test_data = [
            "밥", "택시", "백화점", "뮤지컬", "한양"
        ]
        self.keyword_map = {
            "밥": "식비",
            "택시": "교통",
            "백화점": "쇼핑",
            "뮤지컬": "여가"
        }

    def test_categorize_correctly(self):
        expected = ["식비", "교통", "쇼핑", "여가", "기타"]
        result = categorize(self.test_data, self.keyword_map)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()