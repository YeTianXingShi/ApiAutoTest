from Easy.EasyRequest import EasyRequest

test_a = EasyRequest(user='80663835', application="order-plan-view", env="test")
test_a.start(rid=1)
test_a.start(rid=2)
