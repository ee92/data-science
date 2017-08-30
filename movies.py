import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

data = fetch_movielens(min_rating=4.0)
model = LightFM(loss='warp')
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendation(model, data, user_ids):
	n_users, n_items = data['train'].shape

	for user_id in user_ids:
		known_positives = data['item_labels'][data['train'].tocsr()[user_id].indices]
		scores = model.predict(user_id, np.arange(n_items))
		top = data['item_labels'][np.argsort(-scores)]

		print("User " + str(user_id))
		print("     known positives:")

		for x in known_positives[:3]:
			print("           " + x)

		print("     recommended:")

		for x in top[:3]:
			print("           " + x)

sample_recommendation(model, data, [3, 25, 450])
