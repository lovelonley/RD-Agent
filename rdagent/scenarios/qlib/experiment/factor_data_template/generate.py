import qlib

qlib.init(provider_uri="~/.qlib/qlib_data/cn_data")

from qlib.data import D

instruments = D.instruments("csi1800mb")
fields = [
    "$open", "$close", "$high", "$low", "$volume", "$vwap", 
    "$change", "$factor", "$turnover_rate", 
    "$pe", "$pb", "$ps", "$total_mv", "$circ_mv", 
    "$industry", "$roe", "$netprofit_yoy", "$debt_ratio",
    "$grossprofit_margin", "$eps", "$current_ratio", "$or_yoy", 
    "$q_roe", "$op_yoy", "$bps", "$ocfps",
    "$north_money", "$rzye", 
    "$net_mf_amount", "$large_net_mf", "$elg_net_mf", "$net_mf_amount_ma5"
]
data = D.features(instruments, fields, freq="day").swaplevel().sort_index().loc["2018-12-29":].sort_index()

data.to_hdf("./daily_pv_all.h5", key="data")


data = (
    (
        D.features(instruments, fields, start_time="2018-01-01", end_time="2019-12-31", freq="day")
        .swaplevel()
        .sort_index()
    )
    .swaplevel()
    .loc[data.reset_index()["instrument"].unique()[:100]]
    .swaplevel()
    .sort_index()
)

data.to_hdf("./daily_pv_debug.h5", key="data")
