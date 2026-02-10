from pretexting.core import PretextGenerator,AwarenessTrainer
p=PretextGenerator()
for s in ["tech_support","executive","new_employee"]:
    r=p.generate_scenario(s)
    print(f"{s}: {r['role']} (Urgency: {r['urgency']})")
t=AwarenessTrainer()
good=t.score_response(["verified_identity","reported_incident"])
bad=t.score_response(["gave_credentials","did_not_verify"])
print(f"\nGood response: {good['score']}/100")
print(f"Bad response: {bad['score']}/100")
