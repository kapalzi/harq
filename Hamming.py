class Hamming(object):

    def createHamming(frame):
        frame = bin(frame)

        frame_one = [frame[0], frame[1], frame[2], frame[3]] #dzieli ramke na dwie mniejsze
        frame_two = [frame[4], frame[5], frame[6], frame[7]]

        #dla pierwszej ramki
        pairity_one_one=frame_one[0]+frame_one[1]+frame_one[3] #pierwszy bit kontrolny
        pairity_one_two=frame_one[0]+frame_one[2]+frame_one[3] #drugi bit kontrolny
        pairity_one_three = frame_one[1] + frame_one[2] + frame_one[3] #trzeci bit kontrolny

        frame_one = [pairity_one_one, pairity_one_two, frame_one[0], pairity_one_three, frame_one[1], frame_one[2], frame_one[3]] #dopisanie bitow kontrolnych do ramki

        #dla drugiej ramki
        pairity_two_one = frame_two[0] + frame_two[1] + frame_two[3] #pierwszy bit kontrolny
        pairity_two_two = frame_two[0] + frame_two[2] + frame_two[3] #drugi bit kontrolny
        pairity_two_three = frame_two[1] + frame_two[2] + frame_two[3] #trzeci bit kontrolny

        frame_two = [pairity_two_one, pairity_two_two, frame_two[0], pairity_two_three, frame_two[1], frame_two[2], frame_two[3]] #dopisanie bitow kontrolnych do ramki

        frame = frame_one + frame_two #ponowne polaczenie ramek

        return frame
