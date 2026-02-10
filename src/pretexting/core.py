"""Pretexting Framework"""
import json,random,hashlib
from datetime import datetime

class PretextGenerator:
    SCENARIOS={
        "tech_support":{"role":"IT Support Technician","pretext":"System upgrade requires credential verification",
                        "urgency":"MEDIUM","props":["company badge","laptop","work order"]},
        "vendor":{"role":"Third-party vendor","pretext":"Scheduled maintenance on network equipment",
                  "urgency":"LOW","props":["vendor badge","equipment","work order"]},
        "executive":{"role":"Senior executive","pretext":"Urgent wire transfer or data request",
                     "urgency":"HIGH","props":["executive authority","time pressure"]},
        "auditor":{"role":"Compliance auditor","pretext":"Mandatory security audit requiring system access",
                   "urgency":"MEDIUM","props":["audit notice","clipboard","professional attire"]},
        "new_employee":{"role":"New hire on first day","pretext":"Need help accessing systems and building",
                        "urgency":"LOW","props":["confused demeanor","company materials"]},
    }
    
    def generate_scenario(self,scenario_type):
        base=self.SCENARIOS.get(scenario_type,{})
        return {**base,"type":scenario_type,"generated":datetime.now().isoformat()}
    
    def assess_effectiveness(self,scenario,target_profile):
        score=50
        if target_profile.get("security_training"): score-=20
        if target_profile.get("new_employee"): score+=15
        if target_profile.get("stressed"): score+=10
        if scenario.get("urgency")=="HIGH": score+=15
        return {"effectiveness":min(max(score,0),100),"factors_used":len(target_profile)}

class AwarenessTrainer:
    RED_FLAGS=["Unexpected urgency","Request for credentials","Unusual sender","Bypass normal procedures",
               "Emotional manipulation","Authority pressure","Too good to be true","Request for sensitive data"]
    
    def score_response(self,response_actions):
        score=100
        penalties={"gave_credentials":-40,"clicked_link":-20,"downloaded_attachment":-25,
                   "shared_info":-15,"bypassed_procedure":-20,"did_not_verify":-10}
        bonuses={"verified_identity":10,"reported_incident":15,"contacted_security":10,
                 "refused_request":10,"asked_questions":5}
        for action in response_actions:
            score+=penalties.get(action,bonuses.get(action,0))
        return {"score":max(0,min(100,score)),"actions":response_actions}
    
    def generate_training(self,scenario_type):
        return {"scenario":scenario_type,"red_flags":self.RED_FLAGS,
                "correct_actions":["Verify identity independently","Contact security team",
                                   "Never share credentials","Follow established procedures"]}
