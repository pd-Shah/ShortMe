# How to Run Project
#### 1. First install `docker-compose`([installation guide](https://docs.docker.com/compose/install/)),
#### 2. then just run following commands to run whole project.

```bash
chmod 777 run.sh
./run.sh
```
#### 3. open a new terminal
#### 4. database first time configuration
in the project directory `/ShortMe/settings.py`, in `class Config`, there are two line to config database in the project directory `/ShortMe/settings.py`, in `class Config`, there are two line to config database(`SQLALCHEMY_DATABASE_URI`). comment first line and uncomment the second line.
```python
class Config:
    ...
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database:5432/postgres'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@0.0.0.0:5432/postgres'
```
and run following command in the new terminal:
```python
chmod 777 refresh.sh
./refresh.sh
```
it should be run silently without any error.
### 5.undo the comments
in the project directory `/ShortMe/settings.py`, in `class Config`, there are two line to config database in the project directory `/ShortMe/settings.py`, in `class Config`, there are two line to config database(`SQLALCHEMY_DATABASE_URI`). uncomment first line and comment the second line.
```python
class Config:
    ...
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database:5432/postgres'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@0.0.0.0:5432/postgres'
```
#### 6. Benchmark
here I have test `1000 get request` in two way:
First timing which for 1000 call the results are :
```commandline
4.74492365200058
```
and the second with more details:
```commandline
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1017(_handle_fromlist)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
      2/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
       24    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:342(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:376(cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:389(parent)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:397(has_location)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:477(_init_module_attrs)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:549(module_from_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
      2/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:650(_load_unlocked)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:725(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:800(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:863(__enter__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:867(__exit__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:890(_find_spec)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:956(_find_and_load_unlocked)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:986(_find_and_load)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1010(path_stats)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1265(_path_importer_cache)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1302(_get_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1334(find_spec)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1426(_get_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1431(find_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:294(cache_from_source)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:40(_relax_case)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:424(_get_cached)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:456(_check_name_wrapper)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:493(_classify_pyc)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:51(_unpack_uint32)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:526(_validate_timestamp_pyc)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:578(_compile_bytecode)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_join)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:629(spec_from_file_location)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:64(<listcomp>)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:68(_path_split)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:774(create_module)
      2/1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:777(exec_module)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:80(_path_stat)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:849(get_code)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:90(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:939(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:964(get_filename)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:969(get_data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:99(_path_isfile)
        1    0.011    0.011    6.597    6.597 <string>:1(<listcomp>)
        1    0.000    0.000    6.597    6.597 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 __init__.py:1220(__init__)
     1000    0.003    0.000    0.005    0.000 __init__.py:1272(getLogger)
        1    0.000    0.000    0.000    0.000 __init__.py:1323(_fixupParents)
        1    0.000    0.000    0.000    0.000 __init__.py:1392(__init__)
     2000    0.002    0.000    0.004    0.000 __init__.py:1412(debug)
     1001    0.001    0.000    0.001    0.000 __init__.py:1663(getEffectiveLevel)
     2000    0.002    0.000    0.002    0.000 __init__.py:1677(isEnabledFor)
        1    0.000    0.000    0.000    0.000 __init__.py:189(_checkLevel)
     1000    0.002    0.000    0.007    0.000 __init__.py:2006(getLogger)
     1001    0.001    0.000    0.001    0.000 __init__.py:214(_acquireLock)
     1001    0.000    0.000    0.001    0.000 __init__.py:223(_releaseLock)
     1000    0.004    0.000    0.032    0.000 __init__.py:24(detect)
        1    0.000    0.000    0.000    0.000 __init__.py:43(normalize_encoding)
        1    0.000    0.000    0.000    0.000 __init__.py:70(search_function)
        1    0.000    0.000    0.000    0.000 __init__.py:772(__init__)
     1000    0.006    0.000    0.023    0.000 _collections.py:140(__init__)
    11000    0.009    0.000    0.011    0.000 _collections.py:155(__getitem__)
     8000    0.003    0.000    0.003    0.000 _collections.py:186(__iter__)
     7000    0.004    0.000    0.007    0.000 _collections.py:214(add)
     1000    0.005    0.000    0.015    0.000 _collections.py:230(extend)
     2000    0.002    0.000    0.003    0.000 _collections.py:46(__init__)
     1000    0.002    0.000    0.003    0.000 _collections.py:53(__getitem__)
     1000    0.003    0.000    0.003    0.000 _collections.py:60(__setitem__)
     2000    0.007    0.000    0.064    0.000 _collections.py:91(clear)
       31    0.000    0.000    0.000    0.000 _collections_abc.py:392(__subclasshook__)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:406(__subclasshook__)
    16000    0.015    0.000    0.036    0.000 _collections_abc.py:657(get)
     6000    0.005    0.000    0.016    0.000 _collections_abc.py:664(__contains__)
     8000    0.005    0.000    0.007    0.000 _collections_abc.py:676(items)
     8000    0.002    0.000    0.002    0.000 _collections_abc.py:698(__init__)
     2000    0.001    0.000    0.003    0.000 _collections_abc.py:701(__len__)
        1    0.000    0.000    0.000    0.000 _collections_abc.py:72(_check_methods)
   282000    0.121    0.000    0.601    0.000 _collections_abc.py:742(__iter__)
     8000    0.021    0.000    0.056    0.000 _collections_abc.py:824(update)
     8000    0.002    0.000    0.003    0.000 _internal_utils.py:14(to_native_string)
     1000    0.001    0.000    0.001    0.000 _internal_utils.py:30(unicode_is_ascii)
    15000    0.008    0.000    0.017    0.000 _policybase.py:281(_sanitize_header)
     7000    0.009    0.000    0.014    0.000 _policybase.py:293(header_source_parse)
    15000    0.006    0.000    0.022    0.000 _policybase.py:311(header_fetch_parse)
     32/8    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
    26000    0.007    0.000    0.019    0.000 abc.py:96(__instancecheck__)
     2000    0.008    0.000    0.032    0.000 adapters.py:113(__init__)
     2000    0.005    0.000    0.014    0.000 adapters.py:146(init_poolmanager)
     1000    0.001    0.000    0.002    0.000 adapters.py:203(cert_verify)
     1000    0.007    0.000    0.220    0.000 adapters.py:255(build_response)
     1000    0.004    0.000    0.195    0.000 adapters.py:292(get_connection)
     2000    0.003    0.000    0.069    0.000 adapters.py:319(close)
     1000    0.003    0.000    0.029    0.000 adapters.py:329(request_url)
     1000    0.000    0.000    0.000    0.000 adapters.py:358(add_headers)
     1000    0.013    0.000    5.029    0.005 adapters.py:394(send)
     2000    0.002    0.000    0.002    0.000 adapters.py:58(__init__)
     1000    0.007    0.000    6.516    0.007 api.py:16(request)
     1000    0.009    0.000    6.580    0.007 benchmark.py:5(get_url)
     1000    0.006    0.000    0.017    0.000 client.py:1051(putrequest)
     1000    0.000    0.000    0.001    0.000 client.py:1176(_encode_request)
     1000    0.000    0.000    0.001    0.000 client.py:1180(_validate_path)
     1000    0.001    0.000    0.002    0.000 client.py:1188(_validate_host)
     9000    0.022    0.000    0.040    0.000 client.py:1196(putheader)
     1000    0.002    0.000    0.117    0.000 client.py:1224(endheaders)
     1000    0.001    0.000    0.205    0.000 client.py:1237(request)
     1000    0.013    0.000    0.204    0.000 client.py:1242(_send_request)
     9000    0.004    0.000    0.006    0.000 client.py:1244(<genexpr>)
     1000    0.005    0.000    4.165    0.004 client.py:1288(getresponse)
     1000    0.001    0.000    0.001    0.000 client.py:155(_encode)
     1000    0.016    0.000    0.180    0.000 client.py:200(parse_headers)
     1000    0.003    0.000    0.017    0.000 client.py:233(__init__)
     1000    0.014    0.000    3.936    0.004 client.py:263(_read_status)
     1000    0.012    0.000    4.139    0.004 client.py:296(begin)
     1000    0.001    0.000    0.004    0.000 client.py:376(_check_close)
     1000    0.001    0.000    0.039    0.000 client.py:405(_close_conn)
     1000    0.002    0.000    0.003    0.000 client.py:410(close)
     1000    0.001    0.000    0.001    0.000 client.py:422(flush)
     4000    0.001    0.000    0.001    0.000 client.py:433(isclosed)
     1000    0.005    0.000    0.051    0.000 client.py:443(read)
     1000    0.006    0.000    0.046    0.000 client.py:475(readinto)
     1000    0.004    0.000    0.007    0.000 client.py:815(__init__)
     1000    0.000    0.000    0.000    0.000 client.py:861(_get_hostport)
     2000    0.003    0.000    0.004    0.000 client.py:924(close)
     2000    0.004    0.000    0.109    0.000 client.py:938(send)
    10000    0.003    0.000    0.004    0.000 client.py:976(_output)
     1000    0.005    0.000    0.115    0.000 client.py:997(_send_output)
        1    0.000    0.000    0.000    0.000 codecs.py:94(__new__)
     1000    0.004    0.000    0.011    0.000 connection.py:104(__init__)
     2000    0.001    0.000    0.001    0.000 connection.py:117(host)
     1000    0.000    0.000    0.000    0.000 connection.py:136(host)
     1000    0.003    0.000    0.087    0.000 connection.py:146(_new_conn)
     1000    0.001    0.000    0.001    0.000 connection.py:177(_prepare_conn)
     1000    0.001    0.000    0.090    0.000 connection.py:186(connect)
     1000    0.002    0.000    0.019    0.000 connection.py:190(putrequest)
     1000    0.006    0.000    0.085    0.000 connection.py:33(create_connection)
     1000    0.001    0.000    0.003    0.000 connection.py:89(_set_socket_options)
     1000    0.001    0.000    0.001    0.000 connection.py:97(allowed_gai_family)
     1000    0.001    0.000    0.004    0.000 connectionpool.py:1020(_normalize_host)
     1000    0.011    0.000    0.079    0.000 connectionpool.py:172(__init__)
     1000    0.005    0.000    0.019    0.000 connectionpool.py:221(_new_conn)
     1000    0.002    0.000    0.027    0.000 connectionpool.py:242(_get_conn)
     1000    0.002    0.000    0.015    0.000 connectionpool.py:281(_put_conn)
     1000    0.000    0.000    0.000    0.000 connectionpool.py:309(_validate_conn)
     2000    0.002    0.000    0.007    0.000 connectionpool.py:319(_get_timeout)
     1000    0.015    0.000    4.405    0.004 connectionpool.py:356(_make_request)
     1000    0.007    0.000    0.052    0.000 connectionpool.py:460(close)
     1000    0.019    0.000    4.566    0.005 connectionpool.py:499(urlopen)
     1000    0.002    0.000    0.006    0.000 connectionpool.py:78(__init__)
     2000    0.002    0.000    0.003    0.000 contextlib.py:108(__enter__)
     2000    0.003    0.000    0.023    0.000 contextlib.py:117(__exit__)
     2000    0.002    0.000    0.007    0.000 contextlib.py:238(helper)
     2000    0.004    0.000    0.005    0.000 contextlib.py:82(__init__)
     2000    0.002    0.000    0.003    0.000 cookiejar.py:1008(set_ok_domain)
     2000    0.000    0.000    0.000    0.000 cookiejar.py:1067(set_ok_port)
     6000    0.006    0.000    0.011    0.000 cookiejar.py:1219(vals_sorted_by_key)
     6000    0.003    0.000    0.014    0.000 cookiejar.py:1223(deepvalues)
     4000    0.007    0.000    0.015    0.000 cookiejar.py:1258(__init__)
     1000    0.001    0.000    0.001    0.000 cookiejar.py:1287(_cookies_for_request)
     1000    0.001    0.000    0.002    0.000 cookiejar.py:1294(_cookie_attrs)
     1000    0.004    0.000    0.013    0.000 cookiejar.py:1353(add_cookie_header)
     4000    0.009    0.000    0.009    0.000 cookiejar.py:1386(_normalized_cookie_tuples)
     2000    0.010    0.000    0.063    0.000 cookiejar.py:1483(_cookie_from_cookie_tuple)
     4000    0.004    0.000    0.077    0.000 cookiejar.py:1575(_cookies_from_attrs_set)
     2000    0.002    0.000    0.002    0.000 cookiejar.py:1584(_process_rfc2109_cookies)
     2000    0.014    0.000    0.129    0.000 cookiejar.py:1596(make_cookies)
     2000    0.004    0.000    0.005    0.000 cookiejar.py:1664(set_cookie)
     2000    0.009    0.000    0.247    0.000 cookiejar.py:1677(extract_cookies)
     1000    0.002    0.000    0.005    0.000 cookiejar.py:1731(clear_expired_cookies)
     6000    0.002    0.000    0.002    0.000 cookiejar.py:1750(__iter__)
     2000    0.001    0.000    0.002    0.000 cookiejar.py:341(split_header_words)
     7000    0.001    0.000    0.001    0.000 cookiejar.py:44(_debug)
     2000    0.012    0.000    0.017    0.000 cookiejar.py:459(parse_ns_headers)
     2000    0.001    0.000    0.004    0.000 cookiejar.py:528(is_HDN)
     2000    0.001    0.000    0.002    0.000 cookiejar.py:543(domain_match)
     4000    0.008    0.000    0.043    0.000 cookiejar.py:613(request_host)
     2000    0.002    0.000    0.027    0.000 cookiejar.py:629(eff_request_host)
     2000    0.004    0.000    0.023    0.000 cookiejar.py:640(request_path)
     4000    0.005    0.000    0.026    0.000 cookiejar.py:670(escape_path)
     2000    0.003    0.000    0.008    0.000 cookiejar.py:684(reach)
     2000    0.004    0.000    0.045    0.000 cookiejar.py:719(is_third_party)
     2000    0.006    0.000    0.010    0.000 cookiejar.py:754(__init__)
     4000    0.005    0.000    0.005    0.000 cookiejar.py:877(__init__)
     2000    0.001    0.000    0.001    0.000 cookiejar.py:919(is_blocked)
     2000    0.000    0.000    0.000    0.000 cookiejar.py:934(is_not_allowed)
     2000    0.010    0.000    0.095    0.000 cookiejar.py:942(set_ok)
     2000    0.001    0.000    0.001    0.000 cookiejar.py:961(set_ok_version)
     2000    0.003    0.000    0.049    0.000 cookiejar.py:976(set_ok_verifiability)
     2000    0.001    0.000    0.001    0.000 cookiejar.py:988(set_ok_name)
     2000    0.002    0.000    0.025    0.000 cookiejar.py:997(set_ok_path)
     2000    0.001    0.000    0.001    0.000 cookies.py:104(__init__)
     4000    0.001    0.000    0.001    0.000 cookies.py:111(info)
     2000    0.006    0.000    0.273    0.000 cookies.py:118(extract_cookies_to_jar)
     1000    0.003    0.000    0.025    0.000 cookies.py:135(get_cookie_header)
     2000    0.005    0.000    0.011    0.000 cookies.py:343(set_cookie)
     2000    0.002    0.000    0.005    0.000 cookies.py:348(update)
     3000    0.005    0.000    0.028    0.000 cookies.py:37(__init__)
     2000    0.002    0.000    0.010    0.000 cookies.py:45(get_host)
     2000    0.001    0.000    0.011    0.000 cookies.py:48(get_origin_req_host)
     3000    0.007    0.000    0.032    0.000 cookies.py:508(cookiejar_from_dict)
     6000    0.004    0.000    0.015    0.000 cookies.py:51(get_full_url)
     3000    0.002    0.000    0.012    0.000 cookies.py:521(<listcomp>)
     2000    0.002    0.000    0.008    0.000 cookies.py:529(merge_cookies)
     2000    0.000    0.000    0.000    0.000 cookies.py:65(is_unverifiable)
     1000    0.000    0.000    0.000    0.000 cookies.py:81(get_new_headers)
     2000    0.001    0.000    0.001    0.000 cookies.py:84(unverifiable)
     2000    0.001    0.000    0.012    0.000 cookies.py:88(origin_req_host)
     2000    0.002    0.000    0.003    0.000 copy.py:66(copy)
     2002    0.002    0.000    0.004    0.000 enum.py:278(__call__)
     2002    0.002    0.000    0.002    0.000 enum.py:557(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:659(value)
        1    0.000    0.000    0.000    0.000 enum.py:828(__and__)
     1000    0.005    0.000    0.013    0.000 feedparser.py:101(push)
     2000    0.002    0.000    0.003    0.000 feedparser.py:122(pushlines)
     2000    0.000    0.000    0.000    0.000 feedparser.py:125(__iter__)
    10000    0.004    0.000    0.012    0.000 feedparser.py:128(__next__)
     1000    0.006    0.000    0.013    0.000 feedparser.py:139(__init__)
     1000    0.002    0.000    0.109    0.000 feedparser.py:173(feed)
     2000    0.004    0.000    0.102    0.000 feedparser.py:178(_call_parse)
     1000    0.002    0.000    0.022    0.000 feedparser.py:184(close)
     1000    0.002    0.000    0.003    0.000 feedparser.py:197(_new_message)
     1000    0.001    0.000    0.001    0.000 feedparser.py:210(_pop_message)
     2000    0.015    0.000    0.098    0.000 feedparser.py:218(_parsegen)
     1000    0.015    0.000    0.035    0.000 feedparser.py:471(_parse_headers)
     1000    0.004    0.000    0.004    0.000 feedparser.py:53(__init__)
     1000    0.002    0.000    0.004    0.000 feedparser.py:70(close)
    10000    0.006    0.000    0.007    0.000 feedparser.py:78(readline)
     2000    0.003    0.000    0.018    0.000 genericpath.py:16(exists)
     3000    0.002    0.000    0.003    0.000 hooks.py:17(default_hooks)
     3000    0.001    0.000    0.001    0.000 hooks.py:18(<dictcomp>)
     1000    0.001    0.000    0.001    0.000 hooks.py:23(dispatch_hook)
     1000    0.003    0.000    0.004    0.000 idna.py:147(encode)
        1    0.000    0.000    0.000    0.000 idna.py:300(getregentry)
     2000    0.003    0.000    0.003    0.000 message.py:120(__init__)
     2000    0.001    0.000    0.001    0.000 message.py:181(is_multipart)
     1000    0.003    0.000    0.007    0.000 message.py:213(get_payload)
     4000    0.004    0.000    0.005    0.000 message.py:29(_splitparam)
     1000    0.001    0.000    0.001    0.000 message.py:303(set_payload)
     1000    0.001    0.000    0.012    0.000 message.py:451(items)
     1000    0.003    0.000    0.010    0.000 message.py:459(<listcomp>)
     9000    0.013    0.000    0.028    0.000 message.py:462(get)
     7000    0.003    0.000    0.003    0.000 message.py:479(set_raw)
     4000    0.008    0.000    0.015    0.000 message.py:497(get_all)
     4000    0.007    0.000    0.030    0.000 message.py:564(get_content_type)
     3000    0.002    0.000    0.020    0.000 message.py:588(get_content_maintype)
     1000    0.002    0.000    0.005    0.000 models.py:175(register_hook)
     1000    0.000    0.000    0.000    0.000 models.py:184(<genexpr>)
     1000    0.003    0.000    0.004    0.000 models.py:226(__init__)
     1000    0.001    0.000    0.002    0.000 models.py:291(__init__)
     1000    0.004    0.000    0.198    0.000 models.py:308(prepare)
     1000    0.002    0.000    0.002    0.000 models.py:340(prepare_method)
     1000    0.009    0.000    0.089    0.000 models.py:356(prepare_url)
     1000    0.010    0.000    0.043    0.000 models.py:442(prepare_headers)
     1000    0.003    0.000    0.010    0.000 models.py:453(prepare_body)
     1000    0.002    0.000    0.005    0.000 models.py:522(prepare_content_length)
     1000    0.002    0.000    0.015    0.000 models.py:535(prepare_auth)
     1000    0.002    0.000    0.027    0.000 models.py:557(prepare_cookies)
     1000    0.001    0.000    0.006    0.000 models.py:577(prepare_hooks)
     1000    0.008    0.000    0.028    0.000 models.py:597(__init__)
     1000    0.002    0.000    0.004    0.000 models.py:61(path_url)
     1000    0.001    0.000    0.003    0.000 models.py:708(is_redirect)
     1000    0.002    0.000    0.035    0.000 models.py:725(apparent_encoding)
     1000    0.002    0.000    0.002    0.000 models.py:730(iter_content)
     2000    0.003    0.000    0.100    0.000 models.py:747(generate)
     4000    0.004    0.000    0.108    0.000 models.py:816(content)
     2000    0.003    0.000    0.009    0.000 models.py:82(_encode_params)
     1000    0.004    0.000    0.039    0.000 models.py:836(text)
        1    0.000    0.000    0.000    0.000 netrc.py:1(<module>)
        1    0.000    0.000    0.000    0.000 netrc.py:10(NetrcParseError)
        1    0.000    0.000    0.000    0.000 netrc.py:22(netrc)
   258000    0.140    0.000    0.339    0.000 os.py:670(__getitem__)
   252000    0.066    0.000    0.137    0.000 os.py:693(__iter__)
   258000    0.079    0.000    0.122    0.000 os.py:748(encode)
   500000    0.086    0.000    0.149    0.000 os.py:752(decode)
    39000    0.024    0.000    0.027    0.000 parse.py:110(_coerce_args)
     1000    0.001    0.000    0.002    0.000 parse.py:147(username)
     8000    0.009    0.000    0.022    0.000 parse.py:155(hostname)
     1000    0.001    0.000    0.001    0.000 parse.py:183(_userinfo)
     8000    0.008    0.000    0.011    0.000 parse.py:195(_hostinfo)
     1000    0.001    0.000    0.006    0.000 parse.py:330(geturl)
    16000    0.033    0.000    0.093    0.000 parse.py:366(urlparse)
        1    0.000    0.000    0.000    0.000 parse.py:391(_splitnetloc)
        1    0.000    0.000    0.000    0.000 parse.py:399(_checknetloc)
    19000    0.022    0.000    0.039    0.000 parse.py:417(urlsplit)
     2000    0.003    0.000    0.013    0.000 parse.py:474(urlunparse)
     2000    0.004    0.000    0.006    0.000 parse.py:485(urlunsplit)
     1000    0.002    0.000    0.002    0.000 parse.py:624(unquote)
     5000    0.007    0.000    0.023    0.000 parse.py:787(quote)
     5000    0.009    0.000    0.015    0.000 parse.py:858(quote_from_bytes)
     1000    0.002    0.000    0.002    0.000 parse.py:880(urlencode)
    39000    0.004    0.000    0.004    0.000 parse.py:99(_noop)
     1000    0.001    0.000    0.001    0.000 parser.py:17(__init__)
     1000    0.005    0.000    0.149    0.000 parser.py:41(parse)
     1000    0.006    0.000    0.155    0.000 parser.py:59(parsestr)
     2000    0.005    0.000    0.010    0.000 poolmanager.py:165(__init__)
     1000    0.002    0.000    0.053    0.000 poolmanager.py:168(<lambda>)
     1000    0.004    0.000    0.084    0.000 poolmanager.py:183(_new_pool)
     2000    0.002    0.000    0.066    0.000 poolmanager.py:210(clear)
     1000    0.003    0.000    0.117    0.000 poolmanager.py:219(connection_from_host)
     1000    0.003    0.000    0.113    0.000 poolmanager.py:242(connection_from_context)
     1000    0.004    0.000    0.095    0.000 poolmanager.py:255(connection_from_pool_key)
     1000    0.003    0.000    0.163    0.000 poolmanager.py:279(connection_from_url)
     1000    0.001    0.000    0.001    0.000 poolmanager.py:295(_merge_pool_kwargs)
     1000    0.012    0.000    0.015    0.000 poolmanager.py:74(_default_key_normalizer)
     2000    0.009    0.000    0.024    0.000 posixpath.py:228(expanduser)
     2000    0.001    0.000    0.001    0.000 posixpath.py:41(_get_sep)
     1000    0.001    0.000    0.001    0.000 queue.py:11(_init)
    11000    0.022    0.000    0.058    0.000 queue.py:121(put)
    23000    0.006    0.000    0.008    0.000 queue.py:14(_qsize)
    12000    0.019    0.000    0.050    0.000 queue.py:153(get)
    11000    0.004    0.000    0.005    0.000 queue.py:17(_put)
    11000    0.004    0.000    0.005    0.000 queue.py:20(_get)
     1000    0.004    0.000    0.013    0.000 queue.py:33(__init__)
        1    0.000    0.000    0.000    0.000 re.py:248(compile)
        1    0.000    0.000    0.000    0.000 re.py:287(_compile)
     2000    0.084    0.000    0.664    0.000 request.py:2466(getproxies_environment)
     1000    0.002    0.000    0.343    0.000 request.py:2497(proxy_bypass_environment)
     3000    0.002    0.000    0.002    0.000 request.py:41(__init__)
     1000    0.001    0.000    0.001    0.000 request.py:90(set_file_position)
     1000    0.008    0.000    0.022    0.000 response.py:193(__init__)
     2000    0.001    0.000    0.001    0.000 response.py:249(<genexpr>)
     1000    0.002    0.000    0.017    0.000 response.py:273(release_conn)
     1000    0.004    0.000    0.008    0.000 response.py:315(_init_length)
     1000    0.001    0.000    0.001    0.000 response.py:341(<listcomp>)
     1000    0.002    0.000    0.004    0.000 response.py:367(_init_decoder)
     1000    0.004    0.000    0.012    0.000 response.py:38(assert_header_parsing)
     1000    0.000    0.000    0.000    0.000 response.py:390(_decode)
     2000    0.002    0.000    0.019    0.000 response.py:423(_error_catcher)
     1000    0.008    0.000    0.092    0.000 response.py:480(read)
     2000    0.003    0.000    0.097    0.000 response.py:554(stream)
     1000    0.008    0.000    0.068    0.000 response.py:580(from_httplib)
     1000    0.001    0.000    0.002    0.000 response.py:616(getheader)
     1000    0.001    0.000    0.002    0.000 response.py:634(closed)
     2000    0.002    0.000    0.002    0.000 response.py:7(is_fp_closed)
     2000    0.007    0.000    0.008    0.000 retry.py:162(__init__)
     2000    0.001    0.000    0.001    0.000 retry.py:197(<listcomp>)
     1000    0.002    0.000    0.002    0.000 retry.py:320(_is_method_retryable)
     1000    0.001    0.000    0.003    0.000 retry.py:329(is_retry)
     1000    0.002    0.000    0.011    0.000 sessions.py:144(resolve_redirects)
     1000    0.007    0.000    0.068    0.000 sessions.py:362(__init__)
     1000    0.000    0.000    0.000    0.000 sessions.py:417(__enter__)
     1000    0.001    0.000    0.074    0.000 sessions.py:420(__exit__)
     1000    0.011    0.000    0.343    0.000 sessions.py:423(prepare_request)
     1000    0.009    0.000    6.367    0.006 sessions.py:463(request)
     7000    0.012    0.000    0.070    0.000 sessions.py:50(merge_setting)
     1000    0.017    0.000    5.288    0.005 sessions.py:614(send)
     1000    0.001    0.000    0.012    0.000 sessions.py:665(<listcomp>)
     1000    0.006    0.000    0.723    0.001 sessions.py:689(merge_environment_settings)
     1000    0.002    0.000    0.003    0.000 sessions.py:718(get_adapter)
     1000    0.003    0.000    0.073    0.000 sessions.py:732(close)
     2000    0.003    0.000    0.005    0.000 sessions.py:737(mount)
     3000    0.002    0.000    0.011    0.000 sessions.py:74(<listcomp>)
     2000    0.002    0.000    0.002    0.000 sessions.py:743(<listcomp>)
     1000    0.001    0.000    0.001    0.000 sessions.py:81(merge_hooks)
     1000    0.001    0.000    0.004    0.000 sessions.py:98(get_redirect_target)
        1    0.000    0.000    0.000    0.000 shlex.py:1(<module>)
        1    0.000    0.000    0.000    0.000 shlex.py:19(shlex)
     2000    0.001    0.000    0.002    0.000 six.py:614(itervalues)
     1000    0.001    0.000    0.001    0.000 six.py:939(ensure_str)
     9000    0.004    0.000    0.005    0.000 six.py:959(ensure_text)
     1000    0.009    0.000    0.009    0.000 socket.py:219(__init__)
     1000    0.010    0.000    0.013    0.000 socket.py:301(makefile)
     1000    0.001    0.000    0.031    0.000 socket.py:486(_decref_socketios)
     1000    0.001    0.000    0.029    0.000 socket.py:492(_real_close)
     2000    0.002    0.000    0.031    0.000 socket.py:496(close)
     1000    0.003    0.000    0.003    0.000 socket.py:643(__init__)
     1022    0.004    0.000    3.913    0.004 socket.py:655(readinto)
     2022    0.001    0.000    0.001    0.000 socket.py:694(readable)
     1000    0.003    0.000    0.035    0.000 socket.py:732(close)
     1000    0.003    0.000    0.026    0.000 socket.py:901(getaddrinfo)
     2000    0.002    0.000    0.007    0.000 socket.py:97(_intenum_converter)
        2    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:411(_mk_bitmap)
        2    0.000    0.000    0.000    0.000 sre_compile.py:413(<listcomp>)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
        1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        1    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        1    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
        1    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
        1    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
        1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
       14    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
       11    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
       11    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        2    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:295(_class_escape)
        1    0.000    0.000    0.000    0.000 sre_parse.py:432(_uniq)
        1    0.000    0.000    0.000    0.000 sre_parse.py:435(_parse_sub)
        1    0.000    0.000    0.000    0.000 sre_parse.py:493(_parse)
        1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        1    0.000    0.000    0.000    0.000 sre_parse.py:921(fix_flags)
        1    0.000    0.000    0.000    0.000 sre_parse.py:937(parse)
     6000    0.009    0.000    0.059    0.000 structures.py:42(__init__)
    34000    0.016    0.000    0.020    0.000 structures.py:48(__setitem__)
    35000    0.017    0.000    0.021    0.000 structures.py:53(__getitem__)
     5000    0.004    0.000    0.005    0.000 structures.py:59(__iter__)
    39000    0.007    0.000    0.007    0.000 structures.py:60(<genexpr>)
     3000    0.001    0.000    0.002    0.000 structures.py:62(__len__)
     1000    0.001    0.000    0.014    0.000 structures.py:82(copy)
     3000    0.007    0.000    0.007    0.000 threading.py:222(__init__)
    23000    0.007    0.000    0.011    0.000 threading.py:246(__enter__)
    23000    0.007    0.000    0.009    0.000 threading.py:249(__exit__)
    22000    0.007    0.000    0.012    0.000 threading.py:261(_is_owned)
    22000    0.016    0.000    0.027    0.000 threading.py:341(notify)
     6000    0.003    0.000    0.003    0.000 threading.py:81(RLock)
    12000    0.002    0.000    0.002    0.000 timeout.py:112(_validate_timeout)
     1000    0.002    0.000    0.005    0.000 timeout.py:158(from_float)
     2000    0.002    0.000    0.005    0.000 timeout.py:174(clone)
     1000    0.001    0.000    0.001    0.000 timeout.py:188(start_connect)
     3000    0.001    0.000    0.001    0.000 timeout.py:213(connect_timeout)
     1000    0.001    0.000    0.001    0.000 timeout.py:231(read_timeout)
     4000    0.005    0.000    0.008    0.000 timeout.py:95(__init__)
        1    0.000    0.000    0.000    0.000 types.py:171(__get__)
     1000    0.008    0.000    0.012    0.000 universaldetector.py:111(feed)
     1000    0.002    0.000    0.003    0.000 universaldetector.py:220(close)
     1000    0.004    0.000    0.012    0.000 universaldetector.py:81(__init__)
     1000    0.002    0.000    0.002    0.000 universaldetector.py:94(reset)
     4000    0.033    0.000    0.050    0.000 url.py:210(_encode_invalid_chars)
     2000    0.005    0.000    0.009    0.000 url.py:244(_remove_path_dot_segments)
     3000    0.004    0.000    0.009    0.000 url.py:274(_normalize_host)
     1000    0.002    0.000    0.019    0.000 url.py:320(_encode_target)
     2000    0.020    0.000    0.096    0.000 url.py:330(parse_url)
    12000    0.003    0.000    0.006    0.000 url.py:411(ensure_type)
     2000    0.005    0.000    0.007    0.000 url.py:91(__new__)
     1000    0.001    0.000    0.003    0.000 utils.py:108(super_len)
     1000    0.009    0.000    0.053    0.000 utils.py:169(get_netrc_auth)
     7000    0.011    0.000    0.031    0.000 utils.py:287(to_key_val_list)
     1000    0.001    0.000    0.002    0.000 utils.py:455(_parse_content_type_header)
     1000    0.003    0.000    0.006    0.000 utils.py:480(get_encoding_from_headers)
    16000    0.005    0.000    0.008    0.000 utils.py:51(_has_surrogates)
     1000    0.000    0.000    0.000    0.000 utils.py:519(iter_slices)
     1000    0.002    0.000    0.003    0.000 utils.py:570(unquote_unreserved)
     1000    0.002    0.000    0.009    0.000 utils.py:594(requote_uri)
     2000    0.001    0.000    0.001    0.000 utils.py:677(set_environ)
     1000    0.007    0.000    0.378    0.000 utils.py:699(should_bypass_proxies)
     1000    0.002    0.000    0.009    0.000 utils.py:707(<lambda>)
     1000    0.002    0.000    0.702    0.001 utils.py:760(get_environ_proxies)
     2000    0.006    0.000    0.036    0.000 utils.py:772(select_proxy)
     1000    0.002    0.000    0.002    0.000 utils.py:798(default_user_agent)
     1000    0.002    0.000    0.013    0.000 utils.py:807(default_headers)
     1000    0.003    0.000    0.013    0.000 utils.py:911(get_auth_from_url)
     7000    0.004    0.000    0.011    0.000 utils.py:932(check_header_validity)
    19002    0.006    0.000    0.006    0.000 {built-in method __new__ of type object at 0x9005e0}
    26000    0.012    0.000    0.012    0.000 {built-in method _abc._abc_instancecheck}
     32/8    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 {built-in method _imp._fix_co_filename}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
       10    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
     1000    0.011    0.000    0.016    0.000 {built-in method _socket.getaddrinfo}
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
     1004    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        4    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.__build_class__}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.__import__}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.all}
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.any}
      3/1    0.000    0.000    6.597    6.597 {built-in method builtins.exec}
    26012    0.009    0.000    0.009    0.000 {built-in method builtins.getattr}
    40009    0.008    0.000    0.008    0.000 {built-in method builtins.hasattr}
   464021    0.048    0.000    0.067    0.000 {built-in method builtins.isinstance}
     2000    0.000    0.000    0.000    0.000 {built-in method builtins.iter}
70037/68036    0.010    0.000    0.010    0.000 {built-in method builtins.len}
     1000    0.001    0.000    0.001    0.000 {built-in method builtins.max}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     4000    0.002    0.000    0.021    0.000 {built-in method builtins.next}
    36009    0.003    0.000    0.003    0.000 {built-in method builtins.ord}
     1000    0.015    0.000    0.015    0.000 {built-in method builtins.print}
     6000    0.004    0.000    0.004    0.000 {built-in method builtins.sorted}
        6    0.000    0.000    0.000    0.000 {built-in method from_bytes}
        1    0.000    0.000    0.000    0.000 {built-in method fromkeys}
        2    0.000    0.000    0.000    0.000 {built-in method io.open_code}
        2    0.000    0.000    0.000    0.000 {built-in method marshal.loads}
     2006    0.000    0.000    0.000    0.000 {built-in method posix.fspath}
     2008    0.015    0.000    0.015    0.000 {built-in method posix.stat}
     1000    0.000    0.000    0.000    0.000 {built-in method time.monotonic}
     6000    0.002    0.000    0.002    0.000 {built-in method time.time}
     1000    0.000    0.000    0.000    0.000 {function HTTPResponse.flush at 0x7fd9d5d1f8b0}
     2000    0.001    0.000    0.002    0.000 {function SocketIO.close at 0x7fd9d627c5e0}
     1000    0.028    0.000    0.028    0.000 {function socket.close at 0x7fd9d6273c10}
    23000    0.004    0.000    0.004    0.000 {method '__enter__' of '_thread.lock' objects}
    23000    0.002    0.000    0.002    0.000 {method '__exit__' of '_thread.lock' objects}
     1022    0.000    0.000    0.000    0.000 {method '_checkClosed' of '_io._IOBase' objects}
     1022    0.000    0.000    0.001    0.000 {method '_checkReadable' of '_io._IOBase' objects}
     7001    0.003    0.000    0.003    0.000 {method 'acquire' of '_thread.RLock' objects}
    22000    0.005    0.000    0.005    0.000 {method 'acquire' of '_thread.lock' objects}
    11000    0.001    0.000    0.001    0.000 {method 'append' of 'collections.deque' objects}
    57044    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
     2000    0.001    0.000    0.001    0.000 {method 'clear' of 'collections.OrderedDict' objects}
     1000    0.003    0.000    0.038    0.000 {method 'close' of '_io.BufferedReader' objects}
     1000    0.038    0.000    0.038    0.000 {method 'connect' of '_socket.socket' objects}
     6000    0.002    0.000    0.002    0.000 {method 'copy' of 'dict' objects}
     3000    0.002    0.000    0.002    0.000 {method 'count' of 'bytes' objects}
     4000    0.001    0.000    0.001    0.000 {method 'count' of 'str' objects}
     3000    0.001    0.000    0.001    0.000 {method 'decode' of 'bytearray' objects}
   542000    0.069    0.000    0.069    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   310000    0.036    0.000    0.036    0.000 {method 'encode' of 'str' objects}
     3002    0.001    0.000    0.001    0.000 {method 'endswith' of 'str' objects}
     2000    0.001    0.000    0.001    0.000 {method 'extend' of 'collections.deque' objects}
     4002    0.001    0.000    0.002    0.000 {method 'extend' of 'list' objects}
       10    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
    16004    0.003    0.000    0.003    0.000 {method 'find' of 'str' objects}
     2000    0.002    0.000    0.002    0.000 {method 'format' of 'str' objects}
     9000    0.004    0.000    0.004    0.000 {method 'fullmatch' of 're.Pattern' objects}
    49009    0.011    0.000    0.011    0.000 {method 'get' of 'dict' objects}
     5000    0.001    0.000    0.001    0.000 {method 'groups' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        4    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'isascii' of 'str' objects}
     4000    0.001    0.000    0.001    0.000 {method 'items' of 'collections.OrderedDict' objects}
    16001    0.002    0.000    0.002    0.000 {method 'items' of 'dict' objects}
    12000    0.004    0.000    0.104    0.000 {method 'join' of 'bytes' objects}
    22027    0.003    0.000    0.003    0.000 {method 'join' of 'str' objects}
     8000    0.001    0.000    0.001    0.000 {method 'keys' of 'dict' objects}
   360000    0.038    0.000    0.038    0.000 {method 'lower' of 'str' objects}
     8000    0.002    0.000    0.002    0.000 {method 'lstrip' of 'str' objects}
    27000    0.025    0.000    0.025    0.000 {method 'match' of 're.Pattern' objects}
    34000    0.005    0.000    0.005    0.000 {method 'partition' of 'str' objects}
     1000    0.001    0.000    0.001    0.000 {method 'pop' of 'collections.OrderedDict' objects}
    11000    0.001    0.000    0.001    0.000 {method 'pop' of 'collections.deque' objects}
    20002    0.002    0.000    0.002    0.000 {method 'pop' of 'dict' objects}
     1000    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'pop' of 'set' objects}
     8000    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
        2    0.000    0.000    0.000    0.000 {method 'read' of '_io.BufferedReader' objects}
     2000    0.001    0.000    0.001    0.000 {method 'read' of '_io.StringIO' objects}
     1000    0.002    0.000    0.002    0.000 {method 'readinto' of '_io.BufferedReader' objects}
     9000    0.009    0.000    3.923    0.000 {method 'readline' of '_io.BufferedReader' objects}
     2000    0.005    0.000    0.005    0.000 {method 'readlines' of '_io._IOBase' objects}
     1022    3.908    0.004    3.908    0.004 {method 'recv_into' of '_socket.socket' objects}
     7001    0.001    0.000    0.001    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
     9016    0.001    0.000    0.001    0.000 {method 'rpartition' of 'str' objects}
     5000    0.002    0.000    0.002    0.000 {method 'rstrip' of 'bytes' objects}
    11048    0.002    0.000    0.002    0.000 {method 'rstrip' of 'str' objects}
    18000    0.014    0.000    0.014    0.000 {method 'search' of 're.Pattern' objects}
     4000    0.001    0.000    0.001    0.000 {method 'seek' of '_io.StringIO' objects}
     2000    0.015    0.000    0.015    0.000 {method 'sendall' of '_socket.socket' objects}
     7000    0.003    0.000    0.003    0.000 {method 'setdefault' of 'collections.OrderedDict' objects}
     4000    0.001    0.000    0.001    0.000 {method 'setdefault' of 'dict' objects}
     1000    0.002    0.000    0.002    0.000 {method 'setsockopt' of '_socket.socket' objects}
     2000    0.001    0.000    0.001    0.000 {method 'settimeout' of '_socket.socket' objects}
     1000    0.001    0.000    0.001    0.000 {method 'sort' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'split' of 'bytes' objects}
    19000    0.007    0.000    0.007    0.000 {method 'split' of 'str' objects}
     5000    0.002    0.000    0.002    0.000 {method 'startswith' of 'bytearray' objects}
    28000    0.007    0.000    0.007    0.000 {method 'startswith' of 'str' objects}
    23000    0.003    0.000    0.003    0.000 {method 'strip' of 'str' objects}
     8000    0.005    0.000    0.005    0.000 {method 'sub' of 're.Pattern' objects}
     3000    0.003    0.000    0.003    0.000 {method 'subn' of 're.Pattern' objects}
     1000    0.001    0.000    0.001    0.000 {method 'tobytes' of 'memoryview' objects}
        2    0.000    0.000    0.000    0.000 {method 'translate' of 'bytearray' objects}
     2000    0.000    0.000    0.000    0.000 {method 'truncate' of '_io.StringIO' objects}
     2000    0.000    0.000    0.000    0.000 {method 'update' of 'collections.OrderedDict' objects}
     1000    0.001    0.000    0.001    0.000 {method 'update' of 'dict' objects}
     5000    0.001    0.000    0.001    0.000 {method 'upper' of 'str' objects}
    10000    0.002    0.000    0.002    0.000 {method 'values' of 'collections.OrderedDict' objects}
     2000    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
     1000    0.001    0.000    0.001    0.000 {method 'write' of '_io.StringIO' objects}

```

#### 7. API Calls

##### 7.1 signuo
```commandline
curl --location --request POST '0.0.0.0/api/signup' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "test@gmail.com",
    "password": "1"
}'
```

##### 7.2 login
```commandline 
curl --location --request POST 'http://0.0.0.0/api/login' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4rwWg.prbInPfaA6ff1LGbYKfN3I4hkEo' \
--data-raw '{
    "email": "test@gmail.com",
    "password": "1"
}'
```

##### 7.3 get user urls
```commandline
curl --location --request POST 'http://0.0.0.0/api/get-urls' \
--header 'Authorization: eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjk0MTAxOCwiZXhwIjoxNjAzMDAxMDE4fQ.eyJjb2RlIjo2fQ.bX6yyQwekClCvoP7P0Uz7e3IMw3EHaWzJYixZlw7EgCavh4aSFLuyqr67shabgbEk7d_zSRjEghWjegHGbS5aw' \
--header 'Cookie: session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4rwWg.prbInPfaA6ff1LGbYKfN3I4hkEo'
```

##### 7.4
```commandline

curl --location --request POST 'http://0.0.0.0/api/get-url' \
--header 'Authorization: eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjk0MTAxOCwiZXhwIjoxNjAzMDAxMDE4fQ.eyJjb2RlIjo2fQ.bX6yyQwekClCvoP7P0Uz7e3IMw3EHaWzJYixZlw7EgCavh4aSFLuyqr67shabgbEk7d_zSRjEghWjegHGbS5aw' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4rwWg.prbInPfaA6ff1LGbYKfN3I4hkEo' \
--data-raw '{
    "name": "c0f492edc6"
}'```

###### 7.5
```commandline
curl --location --request POST 'http://0.0.0.0/api/add-url' \
--header 'Authorization: eyJhbGciOiJIUzUxMiIsImlhdCI6MTYwMjkzNjU0MywiZXhwIjoxNjAyOTk2NTQzfQ.eyJjb2RlIjo2fQ.BOcvWJiy-BkImgslI-aZNv-Rk6kntXNgljXxC7lphE9q6xQ_23OzSmSz_qaus43l9IDcv6xj4STMkuz26YBa9A' \
--header 'Content-Type: application/json' \
--header 'Cookie: session=.eJwlzjsOwjAMANC7eGaIP4mdXgbZtSNYWzoh7g4S7wTvDfd11PmA7XVcdYP7M2GDnhOFFrKhRputF1Nl91ozkNpwDbdUYtKypKDFuxg7zoEtTLz7qLGXlaeIOkoLJydid2UmjkDvZlkuOrFsFOIkNF6mjAG_yHXW8d8M-HwBinMujQ.X4re3w.rXNX-zbZgVnIzA0UaW_uB-v87LM' \
--data-raw '{
    "url": "www.google.com"
}'

}'```
