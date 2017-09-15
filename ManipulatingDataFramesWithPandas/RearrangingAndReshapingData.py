'''
Created on Aug 17, 2017

@author: idolchevic
'''
import pandas as pd

filename = 'pennsylvania2012_turnout.csv'
election = pd.read_csv('pennsylvania2012_turnout.csv', index_col=0)
titanic = pd.read_csv('titanic.csv', index_col=0)
weather = pd.read_csv('pittsburgh2013.csv', index_col=0)
users = pd.read_csv('users.csv', index_col=0)


print("---------------------------------------------------")
print("    Pivoting a single variable ")
print("---------------------------------------------------")

# Pivot the users DataFrame: visitors_pivot
visitors_pivot = users.pivot(index='weekday', columns='city',values='visitors')

# Print the pivoted DataFrame
print(visitors_pivot)


print("---------------------------------------------------")
print("   Pivoting all variables  ")
print("---------------------------------------------------")

# Pivot users with signups indexed by weekday and city: signups_pivot
signups_pivot = users.pivot(index='weekday', columns='city', values='signups')

# Print signups_pivot
print(signups_pivot)

# Pivot users pivoted by both signups and visitors: pivot
pivot = users.pivot(index='weekday', columns='city')

# Print the pivoted DataFrame
print(pivot)


print("---------------------------------------------------")
print("    Stacking & unstacking I ")
print("---------------------------------------------------")

users = pd.read_csv('users.csv', index_col=['city','weekday'],usecols=['city','weekday','visitors','signups'])
users = users.sort_index()
# Unstack users by 'weekday': byweekday
byweekday = users.unstack(level='weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))


print("---------------------------------------------------")
print("   Stacking & unstacking II  ")
print("---------------------------------------------------")

# Unstack users by 'city': bycity
bycity = users.unstack(level='city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))


print("---------------------------------------------------")
print("   Restoring the index order  ")
print("---------------------------------------------------")

# Stack 'city' back into the index of bycity: newusers
newusers = bycity.stack(level='city')

# Swap the levels of the index of newusers: newusers
newusers = newusers.swaplevel(0,1)

# Print newusers and verify that the index is not sorted
print(newusers)

# Sort the index of newusers: newusers
newusers = newusers.sort_index()

# Print newusers and verify that the index is now sorted
print(newusers)

# Verify that the new DataFrame is equal to the original
print(newusers.equals(users))

print("---------------------------------------------------")
print("    Adding names for readability ")
print("---------------------------------------------------")
users = pd.read_csv('users.csv', index_col=0)
visitors_by_city_weekday = users.pivot(index='weekday', columns='city',values='visitors')
#visitors_by_city_weekday = visitors_by_city_weekday.sort_index()

#print(visitors_by_city_weekday.info())
#print(pd.melt(visitors_by_city_weekday))
#print(visitors_by_city_weekday)

# Reset the index: visitors_by_city_weekday
visitors_by_city_weekday = visitors_by_city_weekday.reset_index() 

# Print visitors_by_city_weekday
print(visitors_by_city_weekday)

# Melt visitors_by_city_weekday: visitors
visitors = pd.melt(visitors_by_city_weekday, id_vars=['weekday'], value_name='visitors')

# Print visitors
print(visitors)



print("---------------------------------------------------")
print("    Going from wide to long ")
print("---------------------------------------------------")

# Melt users: skinny
skinny = pd.melt(users, id_vars=[],value_vars=['visitors' , 'signups'])

# Print skinny
print(skinny)


print("---------------------------------------------------")
print("    Obtaining key-value pairs with melt() ")
print("---------------------------------------------------")

# Set the new index: users_idx
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx, col_level=0)

# Print the key-value pairs
print(kv_pairs)

print("---------------------------------------------------")
print("    Setting up a pivot table ")
print("---------------------------------------------------")

# Create the DataFrame with the appropriate pivot table: by_city_day
by_city_day = users.pivot_table(index='weekday', columns='city')

# Print by_city_day
print(by_city_day)


print("---------------------------------------------------")
print("    Using other aggregations in pivot tables ")
print("---------------------------------------------------")

# Use a pivot table to display the count of each column: count_by_weekday1
count_by_weekday1 = users.pivot_table(index='weekday',aggfunc='count')

# Print count_by_weekday
print(count_by_weekday1)

# Replace 'aggfunc='count'' with 'aggfunc=len': count_by_weekday2
count_by_weekday2 = count_by_weekday1 = users.pivot_table(index='weekday',aggfunc=len)

# Verify that the same result is obtained
print('==========================================')
print(count_by_weekday1.equals(count_by_weekday2))


print("---------------------------------------------------")
print("    Using margins in pivot tables ")
print("---------------------------------------------------")


# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday',aggfunc='sum')

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total 
signups_and_visitors_total = users.pivot_table(index='weekday',aggfunc='sum',margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)

