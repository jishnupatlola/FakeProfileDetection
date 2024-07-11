pragma solidity ^0.8.0;

contract FakeProfileVerification {
    struct Profile {
        string username;
        bool isVerified;
    }

    mapping(address => Profile) public profiles;

    function verifyProfile(address user, string memory username) public {
        profiles[user] = Profile(username, true);
    }

    function isProfileVerified(address user) public view returns (bool) {
        return profiles[user].isVerified;
    }
}
