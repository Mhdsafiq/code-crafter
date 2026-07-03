```java
public class Main {
    public static boolean isAnagram(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }

        int[] count = new int[256];

        for (char c : str1.toCharArray()) {
            count[c]++;
        }

        for (char c : str2.toCharArray()) {
            count[c]--;
            if (count[c] < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isAnagram("listen", "silent"));  // true
        System.out.println(isAnagram("hello", "world"));  // false
    }
}
```

```python
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    count = [0] * 256

    for c in str1:
        count[ord(c)] += 1

    for c in str2:
        count[ord(c)] -= 1
        if count[ord(c)] < 0:
            return False

    return True

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False
```