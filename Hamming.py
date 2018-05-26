class Hamming(object):

    def createHamming(frame):
        frame=bin(frame)

        frame_one=frame[0:3]
        frame_two=frame[4:7]

        pairity_one_one=frame_one[0]+frame_one[1]+frame_one[3]
        pairity_one_two=frame_one[0]+frame_one[2]+frame_one[3]
        pairity_one_three = frame_one[1] + frame_one[2] + frame_one[3]

        frame_one=[pairity_one_one, pairity_one_two, frame_one[0], pairity_one_three, frame_one[1:3]]

        pairity_two_one = frame_two[0] + frame_two[1] + frame_two[3]
        pairity_two_two = frame_two[0] + frame_two[2] + frame_two[3]
        pairity_two_three = frame_two[1] + frame_two[2] + frame_two[3]

        frame_one = [pairity_two_one, pairity_two_two, frame_two[0], pairity_two_three, frame_two[1:3]]

        return frame_one + frame_two
