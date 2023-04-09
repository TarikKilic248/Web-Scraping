# Common Errors

*First, delete any other code in your `main.py` file. Copy each code snippet below into `main.py` by clicking the copy icon in the top right of each code box. Then, hit `run` and see what errors occur. Fix the errors and press `run` again until you are error free. Click on the `👀 Answer` to compare your code to the correct code.*

## What's Your Tag?
```python
myLinks = soup.find_all({"class":"css-1m051bw"})
```

<details> <summary> 👀 Answer </summary>
  
The most common problem is **not identifying the correct tag**.  Somtimes the text is in the `<a>` tag. Sometimes it's in an `<h>`. Inspect a few links to see what the common class and tag are.

  The tag **must be** the first argument in the `find_all`.
  
```python
myLinks = soup.find_all("a", {"class":"css-1m051bw"})
```

</details>

