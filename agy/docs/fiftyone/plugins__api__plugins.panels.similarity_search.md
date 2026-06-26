---
source_url: https://docs.voxel51.com/plugins/api/plugins.panels.similarity_search.html
---

# plugins.panels.similarity_search#

  * [plugins.panels.similarity_search.constants](plugins__api__plugins.panels.similarity_search.constants.md)
    * [`RunStatus`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus)
      * [`RunStatus.PENDING`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.PENDING)
      * [`RunStatus.RUNNING`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.RUNNING)
      * [`RunStatus.COMPLETED`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.COMPLETED)
      * [`RunStatus.FAILED`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.FAILED)
      * [`RunStatus.encode()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.encode)
      * [`RunStatus.replace()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.replace)
      * [`RunStatus.split()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.split)
      * [`RunStatus.rsplit()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rsplit)
      * [`RunStatus.join()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.join)
      * [`RunStatus.capitalize()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.capitalize)
      * [`RunStatus.casefold()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.casefold)
      * [`RunStatus.title()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.title)
      * [`RunStatus.center()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.center)
      * [`RunStatus.count()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.count)
      * [`RunStatus.expandtabs()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.expandtabs)
      * [`RunStatus.find()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.find)
      * [`RunStatus.partition()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.partition)
      * [`RunStatus.index()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.index)
      * [`RunStatus.ljust()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.ljust)
      * [`RunStatus.lower()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.lower)
      * [`RunStatus.lstrip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.lstrip)
      * [`RunStatus.rfind()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rfind)
      * [`RunStatus.rindex()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rindex)
      * [`RunStatus.rjust()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rjust)
      * [`RunStatus.rstrip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rstrip)
      * [`RunStatus.rpartition()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.rpartition)
      * [`RunStatus.splitlines()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.splitlines)
      * [`RunStatus.strip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.strip)
      * [`RunStatus.swapcase()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.swapcase)
      * [`RunStatus.translate()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.translate)
      * [`RunStatus.upper()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.upper)
      * [`RunStatus.startswith()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.startswith)
      * [`RunStatus.endswith()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.endswith)
      * [`RunStatus.removeprefix()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.removeprefix)
      * [`RunStatus.removesuffix()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.removesuffix)
      * [`RunStatus.isascii()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isascii)
      * [`RunStatus.islower()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.islower)
      * [`RunStatus.isupper()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isupper)
      * [`RunStatus.istitle()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.istitle)
      * [`RunStatus.isspace()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isspace)
      * [`RunStatus.isdecimal()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isdecimal)
      * [`RunStatus.isdigit()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isdigit)
      * [`RunStatus.isnumeric()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isnumeric)
      * [`RunStatus.isalpha()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isalpha)
      * [`RunStatus.isalnum()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isalnum)
      * [`RunStatus.isidentifier()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isidentifier)
      * [`RunStatus.isprintable()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.isprintable)
      * [`RunStatus.zfill()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.zfill)
      * [`RunStatus.format()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.format)
      * [`RunStatus.format_map()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.format_map)
      * [`RunStatus.maketrans()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.RunStatus.maketrans)
    * [`QueryType`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType)
      * [`QueryType.TEXT`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.TEXT)
      * [`QueryType.IMAGE`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.IMAGE)
      * [`QueryType.UPLOAD`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.UPLOAD)
      * [`QueryType.encode()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.encode)
      * [`QueryType.replace()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.replace)
      * [`QueryType.split()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.split)
      * [`QueryType.rsplit()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rsplit)
      * [`QueryType.join()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.join)
      * [`QueryType.capitalize()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.capitalize)
      * [`QueryType.casefold()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.casefold)
      * [`QueryType.title()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.title)
      * [`QueryType.center()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.center)
      * [`QueryType.count()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.count)
      * [`QueryType.expandtabs()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.expandtabs)
      * [`QueryType.find()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.find)
      * [`QueryType.partition()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.partition)
      * [`QueryType.index()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.index)
      * [`QueryType.ljust()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.ljust)
      * [`QueryType.lower()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.lower)
      * [`QueryType.lstrip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.lstrip)
      * [`QueryType.rfind()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rfind)
      * [`QueryType.rindex()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rindex)
      * [`QueryType.rjust()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rjust)
      * [`QueryType.rstrip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rstrip)
      * [`QueryType.rpartition()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.rpartition)
      * [`QueryType.splitlines()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.splitlines)
      * [`QueryType.strip()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.strip)
      * [`QueryType.swapcase()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.swapcase)
      * [`QueryType.translate()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.translate)
      * [`QueryType.upper()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.upper)
      * [`QueryType.startswith()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.startswith)
      * [`QueryType.endswith()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.endswith)
      * [`QueryType.removeprefix()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.removeprefix)
      * [`QueryType.removesuffix()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.removesuffix)
      * [`QueryType.isascii()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isascii)
      * [`QueryType.islower()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.islower)
      * [`QueryType.isupper()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isupper)
      * [`QueryType.istitle()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.istitle)
      * [`QueryType.isspace()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isspace)
      * [`QueryType.isdecimal()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isdecimal)
      * [`QueryType.isdigit()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isdigit)
      * [`QueryType.isnumeric()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isnumeric)
      * [`QueryType.isalpha()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isalpha)
      * [`QueryType.isalnum()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isalnum)
      * [`QueryType.isidentifier()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isidentifier)
      * [`QueryType.isprintable()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.isprintable)
      * [`QueryType.zfill()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.zfill)
      * [`QueryType.format()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.format)
      * [`QueryType.format_map()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.format_map)
      * [`QueryType.maketrans()`](plugins__api__plugins.panels.similarity_search.constants.md#plugins.panels.similarity_search.constants.QueryType.maketrans)
  * [plugins.panels.similarity_search.operators](plugins__api__plugins.panels.similarity_search.operators.md)
    * [`SimilaritySearchOperator`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator)
      * [`SimilaritySearchOperator.config`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.config)
      * [`SimilaritySearchOperator.execute()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.execute)
      * [`SimilaritySearchOperator.add_secrets()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.add_secrets)
      * [`SimilaritySearchOperator.builtin`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.builtin)
      * [`SimilaritySearchOperator.method_to_uri()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.method_to_uri)
      * [`SimilaritySearchOperator.name`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.name)
      * [`SimilaritySearchOperator.resolve_delegation()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_delegation)
      * [`SimilaritySearchOperator.resolve_execution_options()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_execution_options)
      * [`SimilaritySearchOperator.resolve_input()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_input)
      * [`SimilaritySearchOperator.resolve_output()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_output)
      * [`SimilaritySearchOperator.resolve_placement()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_placement)
      * [`SimilaritySearchOperator.resolve_run_name()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_run_name)
      * [`SimilaritySearchOperator.resolve_type()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.resolve_type)
      * [`SimilaritySearchOperator.risk_level`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.risk_level)
      * [`SimilaritySearchOperator.to_json()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.to_json)
      * [`SimilaritySearchOperator.uri`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchOperator.uri)
    * [`InitSimilarityRunOperator`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator)
      * [`InitSimilarityRunOperator.config`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.config)
      * [`InitSimilarityRunOperator.execute()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.execute)
      * [`InitSimilarityRunOperator.add_secrets()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.add_secrets)
      * [`InitSimilarityRunOperator.builtin`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.builtin)
      * [`InitSimilarityRunOperator.method_to_uri()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.method_to_uri)
      * [`InitSimilarityRunOperator.name`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.name)
      * [`InitSimilarityRunOperator.resolve_delegation()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_delegation)
      * [`InitSimilarityRunOperator.resolve_execution_options()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_execution_options)
      * [`InitSimilarityRunOperator.resolve_input()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_input)
      * [`InitSimilarityRunOperator.resolve_output()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_output)
      * [`InitSimilarityRunOperator.resolve_placement()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_placement)
      * [`InitSimilarityRunOperator.resolve_run_name()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_run_name)
      * [`InitSimilarityRunOperator.resolve_type()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.resolve_type)
      * [`InitSimilarityRunOperator.risk_level`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.risk_level)
      * [`InitSimilarityRunOperator.to_json()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.to_json)
      * [`InitSimilarityRunOperator.uri`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.InitSimilarityRunOperator.uri)
    * [`ListSimilarityRunsOperator`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator)
      * [`ListSimilarityRunsOperator.config`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.config)
      * [`ListSimilarityRunsOperator.execute()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.execute)
      * [`ListSimilarityRunsOperator.add_secrets()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.add_secrets)
      * [`ListSimilarityRunsOperator.builtin`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.builtin)
      * [`ListSimilarityRunsOperator.method_to_uri()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.method_to_uri)
      * [`ListSimilarityRunsOperator.name`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.name)
      * [`ListSimilarityRunsOperator.resolve_delegation()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_delegation)
      * [`ListSimilarityRunsOperator.resolve_execution_options()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_execution_options)
      * [`ListSimilarityRunsOperator.resolve_input()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_input)
      * [`ListSimilarityRunsOperator.resolve_output()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_output)
      * [`ListSimilarityRunsOperator.resolve_placement()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_placement)
      * [`ListSimilarityRunsOperator.resolve_run_name()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_run_name)
      * [`ListSimilarityRunsOperator.resolve_type()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.resolve_type)
      * [`ListSimilarityRunsOperator.risk_level`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.risk_level)
      * [`ListSimilarityRunsOperator.to_json()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.to_json)
      * [`ListSimilarityRunsOperator.uri`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.ListSimilarityRunsOperator.uri)
    * [`SimilaritySearchSubscriptionOperator`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator)
      * [`SimilaritySearchSubscriptionOperator.subscription_config`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.subscription_config)
      * [`SimilaritySearchSubscriptionOperator.IS_SSE_OPERATOR`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.IS_SSE_OPERATOR)
      * [`SimilaritySearchSubscriptionOperator.add_secrets()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.add_secrets)
      * [`SimilaritySearchSubscriptionOperator.builtin`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.builtin)
      * [`SimilaritySearchSubscriptionOperator.config`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.config)
      * [`SimilaritySearchSubscriptionOperator.execute()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.execute)
      * [`SimilaritySearchSubscriptionOperator.method_to_uri()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.method_to_uri)
      * [`SimilaritySearchSubscriptionOperator.name`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.name)
      * [`SimilaritySearchSubscriptionOperator.resolve_delegation()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_delegation)
      * [`SimilaritySearchSubscriptionOperator.resolve_execution_options()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_execution_options)
      * [`SimilaritySearchSubscriptionOperator.resolve_input()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_input)
      * [`SimilaritySearchSubscriptionOperator.resolve_output()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_output)
      * [`SimilaritySearchSubscriptionOperator.resolve_placement()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_placement)
      * [`SimilaritySearchSubscriptionOperator.resolve_run_name()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_run_name)
      * [`SimilaritySearchSubscriptionOperator.resolve_type()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.resolve_type)
      * [`SimilaritySearchSubscriptionOperator.risk_level`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.risk_level)
      * [`SimilaritySearchSubscriptionOperator.to_json()`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.to_json)
      * [`SimilaritySearchSubscriptionOperator.uri`](plugins__api__plugins.panels.similarity_search.operators.md#plugins.panels.similarity_search.operators.SimilaritySearchSubscriptionOperator.uri)
  * [plugins.panels.similarity_search.run_manager](plugins__api__plugins.panels.similarity_search.run_manager.md)
    * [`get_head_dataset_id()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.get_head_dataset_id)
    * [`RunManager`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager)
      * [`RunManager.create_run()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.create_run)
      * [`RunManager.get_run()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.get_run)
      * [`RunManager.set_run()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.set_run)
      * [`RunManager.update_run()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.update_run)
      * [`RunManager.set_operator_run_id()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.set_operator_run_id)
      * [`RunManager.find_run_by_operator_id()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.find_run_by_operator_id)
      * [`RunManager.delete_run()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.delete_run)
      * [`RunManager.list_runs()`](plugins__api__plugins.panels.similarity_search.run_manager.md#plugins.panels.similarity_search.run_manager.RunManager.list_runs)



## Module contents#

Similarity search panel.

This panel provides a non-blocking interface for running similarity searches against pre-computed embeddings. Queries run as delegated operations and results are stored as persistent runs that users can browse, apply, clone, and iterate on.

Copyright 2017-2026, Voxel51, Inc.

[voxel51.com](https://voxel51.com/)

  


**Classes:**

`SimilaritySearchPanel`([_builtin]) | Panel for running and managing similarity search queries.  
---|---  
  
class plugins.panels.similarity_search.SimilaritySearchPanel(__builtin =False_)#
    

Bases: [`Panel`](api__fiftyone.operators.panel.md#fiftyone.operators.panel.Panel "fiftyone.operators.panel.Panel")

Panel for running and managing similarity search queries.

**Attributes:**

`config` | The `OperatorConfig` for the operator.  
---|---  
`builtin` | Whether the operator is builtin.  
`name` |   
`risk_level` | The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.  
`uri` | The unique identifier of the operator: `plugin_name/operator_name`.  
  
**Methods:**

`on_load`(ctx) |   
---|---  
`on_unload`(ctx) |   
`get_brain_keys`(ctx) | Refresh available similarity brain keys.  
`list_runs`(ctx) | Refresh the runs list.  
`apply_run`(ctx) | Apply a completed run's results as the current view.  
`delete_run`(ctx) | Delete a run from the store.  
`bulk_delete_runs`(ctx) | Delete multiple runs from the store.  
`clone_run`(ctx) | Return a run's config for pre-filling the new search form.  
`rename_run`(ctx) | Rename a run.  
`on_change_view`(ctx) | Called when the panel navigates between pages.  
`get_sample_media`(ctx) | Return media URLs for the given sample IDs.  
`render`(ctx) | Defines the panel's layout and events.  
`add_secrets`(secrets) | Adds secrets to the operator.  
`execute`(ctx) | Executes the operator.  
`method_to_uri`(method_name) | Converts a method name to a URI.  
`on_startup`(ctx) |   
`resolve_delegation`(ctx) | Returns the resolved _forced_ delegation flag.  
`resolve_execution_options`(ctx) | Returns the resolved execution options.  
`resolve_input`(ctx) | Returns the resolved input property.  
`resolve_output`(ctx) | Returns the resolved output property.  
`resolve_placement`(ctx) | Returns the resolved placement of the operator.  
`resolve_run_name`(ctx) | Returns the resolved run name of the operator.  
`resolve_type`(ctx,Â type) | Returns the resolved input or output property.  
`to_json`() | Returns a JSON representation of the operator.  
  
property config#
    

The `OperatorConfig` for the operator.

on_load(_ctx_)#
    

on_unload(_ctx_)#
    

get_brain_keys(_ctx_)#
    

Refresh available similarity brain keys.

list_runs(_ctx_)#
    

Refresh the runs list.

Accepts an optional `owner` param (`"mine"` or `"all"`) to filter runs server-side. Non-managers are always restricted to their own runs regardless of the requested filter.

apply_run(_ctx_)#
    

Apply a completed runâs results as the current view.

delete_run(_ctx_)#
    

Delete a run from the store.

bulk_delete_runs(_ctx_)#
    

Delete multiple runs from the store.

clone_run(_ctx_)#
    

Return a runâs config for pre-filling the new search form.

rename_run(_ctx_)#
    

Rename a run.

on_change_view(_ctx_)#
    

Called when the panel navigates between pages.

get_sample_media(_ctx_)#
    

Return media URLs for the given sample IDs.

Filepaths are returned as-is by default. In FiftyOne Enterprise, cloud filepaths (e.g. `s3://...`, `gs://...`) are resolved to signed HTTPS URLs so the frontend can render them directly.

render(_ctx_)#
    

Defines the panelâs layout and events.

This method is called after every panel event is called (on load, button callback, context change event, etc).

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property")

add_secrets(_secrets_)#
    

Adds secrets to the operator.

Parameters:
    

**secrets** â a list of secrets

property builtin#
    

Whether the operator is builtin.

execute(_ctx_)#
    

Executes the operator.

Subclasses must implement this method.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

JSON serializable data, or None

method_to_uri(_method_name_)#
    

Converts a method name to a URI.

Parameters:
    

**method_name** â the method name

Returns:
    

a URI

property name#
    

on_startup(_ctx_)#
    

resolve_delegation(_ctx_)#
    

Returns the resolved _forced_ delegation flag.

Subclasses can implement this method to decide if delegated execution should be _forced_ for the given operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

whether the operation should be delegated (True), run immediately (False), or None to defer to `resolve_execution_options()` to specify the available options

resolve_execution_options(_ctx_)#
    

Returns the resolved execution options.

Subclasses can implement this method to define the execution options available for the operation.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.executor.ExecutionOptions`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionOptions "fiftyone.operators.executor.ExecutionOptions") instance

resolve_input(_ctx_)#
    

Returns the resolved input property.

Subclasses can implement this method to define the inputs to the operator. This method should never be called directly. Instead use `resolve_type()`.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called each time the input changes.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_output(_ctx_)#
    

Returns the resolved output property.

Subclasses can implement this method to define the outputs of the operator.

By default, this method is called once when the operator is created. If the operator is dynamic, this method is called after the operator is executed.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

resolve_placement(_ctx_)#
    

Returns the resolved placement of the operator.

Subclasses can implement this method to define the placement of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a [`fiftyone.operators.types.Placement`](api__fiftyone.operators.types.md#fiftyone.operators.types.Placement "fiftyone.operators.types.Placement"), or None

resolve_run_name(_ctx_)#
    

Returns the resolved run name of the operator.

Subclasses can implement this method to define the run name of the operator.

Parameters:
    

**ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

Returns:
    

a string, or None

resolve_type(_ctx_ , _type_)#
    

Returns the resolved input or output property.

Parameters:
    

  * **ctx** â the [`fiftyone.operators.executor.ExecutionContext`](api__fiftyone.operators.executor.md#fiftyone.operators.executor.ExecutionContext "fiftyone.operators.executor.ExecutionContext")

  * **type** â the type of property to resolve, either `"inputs"` or `"outputs"`



Returns:
    

a [`fiftyone.operators.types.Property`](api__fiftyone.operators.types.md#fiftyone.operators.types.Property "fiftyone.operators.types.Property"), or None

property risk_level#
    

The effective risk level of the operator, which is used by guardrail systems of an agent to classify tool calls.

to_json()#
    

Returns a JSON representation of the operator.

Returns:
    

a JSON dict

property uri#
    

The unique identifier of the operator: `plugin_name/operator_name`.

IN THIS ARTICLE 
  *[*]: Keyword-only parameters separator (PEP 3102)
