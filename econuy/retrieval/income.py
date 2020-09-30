from os import PathLike
from typing import Union
from urllib.error import URLError, HTTPError

import pandas as pd
from opnieuw import retry
from pandas.tseries.offsets import MonthEnd
from sqlalchemy.engine.base import Connection, Engine

from econuy.utils import ops, metadata
from econuy.utils.lstrings import urls


@retry(
    retry_on_exceptions=(HTTPError, URLError),
    max_calls_total=4,
    retry_window_after_first_call_in_seconds=60,
)
def get_household(update_loc: Union[str, PathLike,
                                Engine, Connection, None] = None,
              revise_rows: Union[str, int] = "nodup",
              save_loc: Union[str, PathLike,
                              Engine, Connection, None] = None,
              name: str = "household_income",
              index_label: str = "index",
              only_get: bool = False) -> pd.DataFrame:
    """Get average household income.

    Parameters
    ----------
    update_loc : str, os.PathLike, SQLAlchemy Connection or Engine, or None, \
                  default None
        Either Path or path-like string pointing to a directory where to find
        a CSV for updating, SQLAlchemy connection or engine object, or
        ``None``, don't update.
    revise_rows : {'nodup', 'auto', int}
        Defines how to process data updates. An integer indicates how many rows
        to remove from the tail of the dataframe and replace with new data.
        String can either be ``auto``, which automatically determines number of
        rows to replace from the inferred data frequency, or ``nodup``,
        which replaces existing periods with new data.
    save_loc : str, os.PathLike, SQLAlchemy Connection or Engine, or None, \
                default None
        Either Path or path-like string pointing to a directory where to save
        the CSV, SQL Alchemy connection or engine object, or ``None``,
        don't save.
    name : str, default 'household_income'
        Either CSV filename for updating and/or saving, or table name if
        using SQL.
    index_label : str, default 'index'
        Label for SQL indexes.
    only_get : bool, default False
        If True, don't download data, retrieve what is available from
        ``update_loc``.

    Returns
    -------
    Monthly average household income : pd.DataFrame

    """
    if only_get is True and update_loc is not None:
        output = ops._io(operation="update", data_loc=update_loc,
                         name=name, index_label=index_label)
        if not output.equals(pd.DataFrame()):
            return output

    raw = pd.read_excel(urls["household_income"]["dl"]["main"], sheet_name="Mensual",
                        skiprows=5, index_col=0).dropna(how="all")
    raw.index = pd.to_datetime(raw.index)
    output = raw.loc[~pd.isna(raw.index)]
    output.index = output.index + MonthEnd(0)
    output.columns = ["Total país", "Montevideo", "Interior: total",
                      "Interior: localidades de más de 5 mil hab.",
                      "Interior: localidades pequeñas y rural"]

    missing = pd.read_excel(urls["household_income"]["dl"]["missing"],
                            index_col=0, header=0).iloc[:, 10:13]
    missing.columns = output.columns[:3]
    output = output.append(missing, sort=False)

    if update_loc is not None:
        previous_data = ops._io(operation="update",
                                data_loc=update_loc,
                                name=name,
                                index_label=index_label)
        output = ops._revise(new_data=output, prev_data=previous_data,
                             revise_rows=revise_rows)

    metadata._set(output, area="Ingresos", currency="UYU",
                  inf_adj="No", unit="Pesos", seas_adj="NSA",
                  ts_type="Flujo", cumperiods=1)

    if save_loc is not None:
        ops._io(operation="save", data_loc=save_loc,
                data=output, name=name, index_label=index_label)

    return output


@retry(
    retry_on_exceptions=(HTTPError, URLError),
    max_calls_total=4,
    retry_window_after_first_call_in_seconds=60,
)
def get_capita(update_loc: Union[str, PathLike,
                                    Engine, Connection, None] = None,
                  revise_rows: Union[str, int] = "nodup",
                  save_loc: Union[str, PathLike,
                                  Engine, Connection, None] = None,
                  name: str = "capita_income",
                  index_label: str = "index",
                  only_get: bool = False) -> pd.DataFrame:
    """Get average per capita income.

    Parameters
    ----------
    update_loc : str, os.PathLike, SQLAlchemy Connection or Engine, or None, \
                  default None
        Either Path or path-like string pointing to a directory where to find
        a CSV for updating, SQLAlchemy connection or engine object, or
        ``None``, don't update.
    revise_rows : {'nodup', 'auto', int}
        Defines how to process data updates. An integer indicates how many rows
        to remove from the tail of the dataframe and replace with new data.
        String can either be ``auto``, which automatically determines number of
        rows to replace from the inferred data frequency, or ``nodup``,
        which replaces existing periods with new data.
    save_loc : str, os.PathLike, SQLAlchemy Connection or Engine, or None, \
                default None
        Either Path or path-like string pointing to a directory where to save
        the CSV, SQL Alchemy connection or engine object, or ``None``,
        don't save.
    name : str, default 'capita_income'
        Either CSV filename for updating and/or saving, or table name if
        using SQL.
    index_label : str, default 'index'
        Label for SQL indexes.
    only_get : bool, default False
        If True, don't download data, retrieve what is available from
        ``update_loc``.

    Returns
    -------
    Monthly average per capita income : pd.DataFrame

    """
    if only_get is True and update_loc is not None:
        output = ops._io(operation="update", data_loc=update_loc,
                         name=name, index_label=index_label)
        if not output.equals(pd.DataFrame()):
            return output

    raw = pd.read_excel(urls["capita_income"]["dl"]["main"],
                        sheet_name="Mensuall", skiprows=5,
                        index_col=0).dropna(how="all")
    raw.index = pd.to_datetime(raw.index)
    output = raw.loc[~pd.isna(raw.index)]
    output.index = output.index + MonthEnd(0)
    output.columns = ["Total país", "Montevideo", "Interior: total",
                      "Interior: localidades de más de 5 mil hab.",
                      "Interior: localidades pequeñas y rural"]

    missing = pd.read_excel(urls["capita_income"]["dl"]["missing"],
                            index_col=0, header=0).iloc[:, 13:16]
    missing.columns = output.columns[:3]
    output = output.append(missing, sort=False)

    if update_loc is not None:
        previous_data = ops._io(operation="update",
                                data_loc=update_loc,
                                name=name,
                                index_label=index_label)
        output = ops._revise(new_data=output, prev_data=previous_data,
                             revise_rows=revise_rows)

    metadata._set(output, area="Ingresos", currency="UYU",
                  inf_adj="No", unit="Pesos", seas_adj="NSA",
                  ts_type="Flujo", cumperiods=1)

    if save_loc is not None:
        ops._io(operation="save", data_loc=save_loc,
                data=output, name=name, index_label=index_label)

    return output