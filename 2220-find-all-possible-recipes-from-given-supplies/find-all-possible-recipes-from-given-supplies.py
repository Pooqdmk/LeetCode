class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        l=[]
        d={recipes[i]:ingredients[i] for i in range(len(recipes))}
        k=0
        while(k<len(recipes)):
            for key,value in d.items():
                if set(value).issubset(set(supplies)) and key not in l:
                    l.append(key)
                    supplies.append(key)
            k=k+1

        # for key,value in d.items():
        #     if set(value).issubset(set(supplies)) and key not in l:
        #         l.append(key)
        
        return l
