class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        return (s.toLowerCase().replaceAll(/\W/g, '') == [...s.toLowerCase().replaceAll(/\W/g, '')].reverse().join(''))
    }
}
