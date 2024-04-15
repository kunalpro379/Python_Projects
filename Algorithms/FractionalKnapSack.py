class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        final_val = 0.0
        remaining_space = truckSize

        for box_count, unit_count in boxTypes:
            if remaining_space >= box_count:
                final_val += box_count * unit_count
                remaining_space -= box_count
            else:
                final_val += remaining_space * unit_count
                break

        return final_val

if __name__ == "__main__":
    solution = Solution()
    boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize = 10
    max_units = solution.maximumUnits(boxTypes, truckSize)
    print("Maximum units that can be loaded:", max_units)
