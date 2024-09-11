class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        for idx, recipe in enumerate(recipes):
            for ing in ingredients[idx]:
                adj[ing].append(recipe)
                indegrees[recipe] += 1
        ans = []
        q = deque(supplies)
        recipes = set(recipes)
        while q:
            x = q.popleft()
            if x in recipes:
                ans.append(x)
            for i in adj[x]:
                indegrees[i] -= 1
                if not indegrees[i]:
                    q.append(i)
        return ans

