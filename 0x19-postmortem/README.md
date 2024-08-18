# 0x19-postmortem

## By Hassan Akinade

# Postmortem: InstaFoodie Outage - August 14, 2024

## Issue Summary

**Duration**: August 14, 2024, 10:00 AM - 11:15 AM (EST)

On August 14, 2024, our flagship service, **InstaFoodie**, experienced a 75-minute outage due to a catastrophic failure of our automatic "FoodieFinder" recommendation engine. During the outage, 85% of our users were unable to load personalized recommendations, leading to mass confusion and an unexpected spike in healthy eating (as users had to make decisions without our usual deep-fried guidance). The root cause was traced back to a rogue pizza emoji that brought down our Redis cache in a cheesy blaze of glory.

## Timeline

- **10:00 AM** - Issue detected by monitoring alert; CPU usage on the Redis cache spiked to 100%.
- **10:02 AM** - On-call engineer receives alert and begins initial investigation.
- **10:05 AM** - Customer complaints flood in via Twitter: "Where are my fried chicken recs?!"
- **10:10 AM** - Assumed cause: suspected DDoS attack. Investigation into incoming traffic begins.
- **10:20 AM** - Network team escalated the issue to the DevOps team.
- **10:30 AM** - Misleading path: Engineers explore a potential bug in the load balancer configuration.
- **10:45 AM** - Realization that Redis cache was unresponsive; further investigation into cache health.
- **10:55 AM** - Discovery of the issue: A malformed pizza emoji in a user request caused a Redis keyspace explosion.
- **11:00 AM** - Redis cache flushed, and emergency deployment of an emoji filter hotfix initiated.
- **11:15 AM** - System stabilized; full service restored.

## Root Cause and Resolution

**Root Cause**: The root cause was a unique and unexpected case of emoji-induced chaos. A single malformed pizza emoji (🍕) entered our system through a user’s search query. Due to a bug in our string handling process, the emoji triggered an infinite loop in our Redis caching layer, causing it to generate thousands of keys per second. The cache eventually became overwhelmed, leading to the service disruption.

**Resolution**: To resolve the issue, we first flushed the Redis cache to clear the keyspace and restore normal operation. Next, we deployed an emergency patch that filtered out malformed emojis before they could interact with the cache. Additionally, we implemented a rate-limiting mechanism on our input processing to prevent similar issues from overwhelming the system in the future.

## Corrective and Preventative Measures

**Improvements & Fixes**:
- Implemented a more robust input validation process to handle emojis and other special characters.
- Enhanced monitoring for Redis to detect unusual key creation patterns and spikes in real-time.
- Increased redundancy in our caching system to prevent single points of failure.
- Added customer-facing error handling to gracefully manage unexpected input without disrupting service.

**Tasks**:
1. Patch Redis cache to prevent keyspace explosion from unhandled inputs.
2. Deploy input sanitization updates across all user input fields.
3. Configure Redis monitoring to alert on rapid key creation.
4. Set up a war room pizza fund for any future pizza-related incidents.
