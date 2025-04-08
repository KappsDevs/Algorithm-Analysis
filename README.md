## 📚 Algorithms Study Repository

This repository is based on the book **"Introduction to Algorithms"** by Cormen.  
I will use it to study algorithm theory and practice, especially for academic purposes.

### 🧠 Merge Sort Analysis

![Merge Sort Tree 1](https://github.com/user-attachments/assets/abdb5206-6285-4ed4-8576-5542bad1b633)  
![Merge Sort Tree 2](https://github.com/user-attachments/assets/9d0195f5-fd68-41c7-9d0f-8f161ccae8f8)

At the end of both trees, we reach the base case: `T(1)` or a constant `C`, which represents a trivial case.

- **Tree height:**  
  n / 2^d = 1 ⟹ d = log₂(n)

- **Cost per level:**  
  Level 0: `cn`  
  Level 1: `cn/2 + cn/2 = cn`  
  Level 2: `cn/4 + cn/4 + cn/4 + cn/4 = cn`  
  ...  
  So, each level has a total cost of `cn`.

- **Total cost:**  
   Height × Cost per level = cn × log₂(n)

### ✅ Conclusion

We can conclude that **Merge Sort** has a time complexity of:  
**O(n log n)**
