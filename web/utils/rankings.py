import os
import pandas as pd

from web.app import config


def get_raw_df():
    df = pd.read_csv(os.path.join(config.APP_ROOT, 'data/test_data.csv'),
                     columns=['user, full_name', 'is_winner', 'timestamp', 'is_redeemed'])
    return df


def get_summary_stats(df):
    """
    Check if someone is on a streak
    Aggregate counts of winners

    returns dictionary with:
        - k (user), v (count)
        - on_streak: BOOL
        - user_on_streak: user
        - streak_count: int
    """
    # grouped = df.groupby(df['user'])
