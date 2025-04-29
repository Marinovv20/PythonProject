from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from rapidfuzz import process

class AddressAutocompleteModel:
    def __init__(self, address_list, n_suggestions=5):
        self.addresses = address_list
        self.n_suggestions = n_suggestions
        self.vectorizer = TfidfVectorizer()
        self.nn_model = NearestNeighbors(n_neighbors=n_suggestions, metric='cosine')
        self._fit()

    def _fit(self):
        self.address_vectors = self.vectorizer.fit_transform(self.addresses)
        self.nn_model.fit(self.address_vectors)

    def suggest(self, query):
        fuzzy_matches = process.extract(query, self.addresses, limit=10, score_cutoff=60)
        candidates = [match[0] for match in fuzzy_matches]
        if not candidates:
            candidates = self.addresses
        query_vec = self.vectorizer.transform([query])
        distances, indices = self.nn_model.kneighbors(query_vec)
        return [self.addresses[i] for i in indices[0] if self.addresses[i] in candidates]
