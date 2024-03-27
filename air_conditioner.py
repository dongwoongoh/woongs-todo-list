def solution(temperature, t1, t2, a, b, onboard):
  mintemp, maxtemp = t1, t2
  dp = [[1e9] * 51 for _ in range(1001)]
  dp[0][temperature + 10] = 0

  for t, is_onboard in enumerate(onboard[1:], 1):
    if is_onboard:
      mintemp_to_consider = mintemp
      maxtemp_to_consider = maxtemp + 1
    else:
      mintemp_to_consider = -10
      maxtemp_to_consider = 40 + 1

    for temp in range(mintemp_to_consider, maxtemp_to_consider):
      if temp == temperature:
        candidates = [dp[t - 1][temp + 10]]
        if temp + 10 != 0:
          candidates.append(dp[t - 1][temp - 1 + 10])
        if temp + 10 != 50:
          candidates.append(dp[t - 1][temp + 1 + 10])

        dp[t][temp + 10] = min(candidates)

      elif temp > temperature:
        candidates = [dp[t - 1][temp + 10] + b]
        if temp + 10 != 0:
          candidates.append(dp[t - 1][temp - 1 + 10] + a)
        if temp + 10 != 50:
          candidates.append(dp[t - 1][temp + 1 + 10])

        dp[t][temp + 10] = min(candidates)
      else:
        candidates = [dp[t - 1][temp + 10] + b]
        if temp + 10 != 0:
          candidates.append(dp[t - 1][temp - 1 + 10])
        if temp + 10 != 50:
          candidates.append(dp[t - 1][temp + 1 + 10] + a)

        dp[t][temp + 10] = min(candidates)

  answer = min(dp[len(onboard) - 1])
  return answer
