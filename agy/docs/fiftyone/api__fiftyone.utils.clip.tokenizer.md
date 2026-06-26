---
source_url: https://docs.voxel51.com/api/fiftyone.utils.clip.tokenizer.html
---

# fiftyone.utils.clip.tokenizer#

CLIP text tokenizer from [openai/CLIP](https://github.com/openai/CLIP).

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Functions:**

`default_bpe`() |   
---|---  
`bytes_to_unicode`() | Returns a list of utf-8 bytes and a corresponding list of unicode strings.  
`get_pairs`(word) | Returns the set of symbol pairs in a word.  
`basic_clean`(text) |   
`whitespace_clean`(text) |   
  
**Classes:**

`SimpleTokenizer`([bpe_path]) |   
---|---  
  
fiftyone.utils.clip.tokenizer.default_bpe()#
    

fiftyone.utils.clip.tokenizer.bytes_to_unicode()#
    

Returns a list of utf-8 bytes and a corresponding list of unicode strings.

The reversible bpe codes work on unicode strings.

This means you need a large # of unicode characters in your vocab if you want to avoid UNKs.

When youâre at something like a 10B token dataset you end up needing around 5K for decent coverage. This is a significant percentage of your normal, say, 32K bpe vocab. To avoid that, we want lookup tables between utf-8 bytes and unicode strings.

And avoids mapping to whitespace/control characters the bpe code barfs on.

fiftyone.utils.clip.tokenizer.get_pairs(_word_)#
    

Returns the set of symbol pairs in a word.

`word` is represented as tuple of symbols (symbols being variable-length strings).

fiftyone.utils.clip.tokenizer.basic_clean(_text_)#
    

fiftyone.utils.clip.tokenizer.whitespace_clean(_text_)#
    

class fiftyone.utils.clip.tokenizer.SimpleTokenizer(_bpe_path : str = '/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/site-packages/fiftyone/utils/clip/bpe_simple_vocab_16e6.txt.gz'_)#
    

Bases: `object`

**Methods:**

`bpe`(token) |   
---|---  
`encode`(text) |   
`decode`(tokens) |   
  
bpe(_token_)#
    

encode(_text_)#
    

decode(_tokens_)#
    

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
  *[/]: Positional-only parameter separator (PEP 570)
