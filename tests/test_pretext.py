import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from pretexting.core import PretextGenerator,AwarenessTrainer

class TestPretext(unittest.TestCase):
    def test_generate(self):
        p=PretextGenerator()
        r=p.generate_scenario("tech_support")
        self.assertEqual(r["role"],"IT Support Technician")
    def test_effectiveness(self):
        p=PretextGenerator()
        r=p.assess_effectiveness({"urgency":"HIGH"},{"new_employee":True})
        self.assertGreater(r["effectiveness"],50)

class TestTrainer(unittest.TestCase):
    def test_score_good(self):
        t=AwarenessTrainer()
        r=t.score_response(["verified_identity","reported_incident","refused_request"])
        self.assertGreater(r["score"],100)
    def test_score_bad(self):
        t=AwarenessTrainer()
        r=t.score_response(["gave_credentials","clicked_link"])
        self.assertLess(r["score"],50)

if __name__=="__main__": unittest.main()
