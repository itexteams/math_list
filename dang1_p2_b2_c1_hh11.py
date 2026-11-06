import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang1_p2_b2_c1_hh11(self):
            # Khai báo biến
            # Nội dung câu hỏi
            noidungcauhoi = '''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. \n'''

            hinhve=(
                            '\\begin{center}  \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                            '\\clip(-1.0040447716306522,-0.8932150776053206) rectangle (6.942754237063268,6.070200776166604); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (6.,2.); \n'
                            '\\draw [line width=1.pt] (6.,2.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt] (0.,0.)-- (3.,5.); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,5.)-- (2.,2.); \n'
                            '\\draw [line width=1.pt] (3.,5.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt] (3.,5.)-- (6.,2.); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,0.); \n'
                            '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,2.); \n'
                            '\\draw (2.71,5.6) node[anchor=north west] {S}; \n'
                            '\\draw (1.4,2.4) node[anchor=north west] {A}; \n'
                            '\\draw (-0.65,0) node[anchor=north west] {B}; \n'
                            '\\draw (3.9,0) node[anchor=north west] {C}; \n'
                            '\\draw (6,2.47) node[anchor=north west] {D}; \n'
                        '\\end{tikzpicture}  \n'
                    '\\end{center}  \n'
                    )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $AB$ và $CD$ song song với nhau'
            nb_da_1_s = '$AB$ và $CD$ cắt nhau'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True $AD$ và $BC$ song song với nhau'
            nb_da_2_s = '$AD$ và $BC$ chéo nhau'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('$AB$ và $CD$ cùng nằm trên mặt phẳng $(ABCD)$ và không có điểm chung nên $AB$ và $CD$ song song với nhau.'
                        )
            loigiai_nb_2 = ('$AD$ và $BC$ cùng nằm trên mặt phẳng $(ABCD)$ và không có điểm chung nên $AD$ và $BC$ song song với nhau.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True $SA$ và $SB$ cắt nhau'
            th_da_1_s = '$SA$ và $SB$ song song với nhau'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $SB$ và $SC$ cắt nhau'
            th_da_2_s = '$SB$ và $SC$ trùng nhau'
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $SC$ và $SD$ cắt nhau'
            th_da_3_s = '$SC$ và $SD$ chéo nhau'
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            th_da_4_d = '\\True $SD$ và $SA$ cắt nhau'
            th_da_4_s = '$SD$ và $SA$ song song nhau'
            list_th_da_4=[th_da_4_d,th_da_4_s]
            th_da_4=random.choice(list_th_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2, th_da_3, th_da_4]

            # Nội dung lời giải
            loigiai_th_1 = ('$SA$ và $SB$ cắt nhau tại $S$.'
                        )
            loigiai_th_2 = ('$SB$ và $SC$ cắt nhau tại $S$.'
                        )
            loigiai_th_3 = ('$SC$ và $SD$ cắt nhau tại $S$.'
                        )
            loigiai_th_4 = ('$SD$ và $SA$ cắt nhau tại $S$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2,loigiai_th_3,loigiai_th_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True $SA$ và $BC$ chéo nhau'
            vd_da_1_s = '$SA$ và $BC$ cắt nhau'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True $SA$ và $CD$ chéo nhau'
            vd_da_2_s = '$SA$ và $CD$ song song'
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]
            vd_da_2=random.choice(list_vd_da_2)

            vd_da_3_d = '\\True $SB$ và $AD$ chéo nhau'
            vd_da_3_s = '$SB$ và $AD$ cắt nhau'
            list_vd_da_3=[vd_da_3_d,vd_da_3_s]
            vd_da_3=random.choice(list_vd_da_3)

            vd_da_4_d = '\\True $SB$ và $CD$ chéo nhau'
            vd_da_4_s = '$SD$ và $CD$ song song'
            list_vd_da_4=[vd_da_4_d,vd_da_4_s]
            vd_da_4=random.choice(list_vd_da_4)

            vd_da_5_d = '\\True $SC$ và $AB$ chéo nhau'
            vd_da_5_s = '$SC$ và $AB$ cắt nhau'
            list_vd_da_5=[vd_da_5_d,vd_da_5_s]
            vd_da_5=random.choice(list_vd_da_5)

            vd_da_6_d = '\\True $SC$ và $AD$ chéo nhau'
            vd_da_6_s = '$SC$ và $AD$ song song'
            list_vd_da_6=[vd_da_6_d,vd_da_6_s]
            vd_da_6=random.choice(list_vd_da_6)

            vd_da_7_d = '\\True $SD$ và $AB$ chéo nhau'
            vd_da_7_s = '$SD$ và $AB$ song song'
            list_vd_da_7=[vd_da_7_d,vd_da_7_s]
            vd_da_7=random.choice(list_vd_da_7)

            vd_da_8_d = '\\True $SD$ và $BC$ chéo nhau'
            vd_da_8_s = '$SD$ và $BC$ song song'
            list_vd_da_8=[vd_da_8_d,vd_da_8_s]
            vd_da_8=random.choice(list_vd_da_8)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2,vd_da_3,vd_da_4,vd_da_5,vd_da_6,vd_da_7,vd_da_8]

            # Nội dung lời giải
            loigiai_vd_1 = ('$SA$ và $BC$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_2 = ('$SA$ và $CD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_3 = ('$SB$ và $AD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_4 = ('$SB$ và $CD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_5 = ('$SC$ và $AB$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_6 = ('$SC$ và $AD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_7 = ('$SD$ và $AB$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vd_8 = ('$SD$ và $BC$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2,loigiai_vd_3,loigiai_vd_4,loigiai_vd_5,loigiai_vd_6,loigiai_vd_7,loigiai_vd_8]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $SA$ và $BD$ chéo nhau'
            vdc_da_1_s = '$SA$ và $BD$ cắt nhau'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True $SB$ và $AC$ chéo nhau'
            vdc_da_2_s = '$SB$ và $AC$ song song'
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
            vdc_da_2=random.choice(list_vdc_da_2)

            vdc_da_3_d = '\\True $SC$ và $BD$ chéo nhau'
            vdc_da_3_s = '$SC$ và $BD$ song song'
            list_vdc_da_3=[vdc_da_3_d,vdc_da_3_s]
            vdc_da_3=random.choice(list_vdc_da_3)

            vdc_da_4_d = '\\True $SD$ và $AC$ chéo nhau'
            vdc_da_4_s = '$SD$ và $AC$ cắt nhau'
            list_vdc_da_4=[vdc_da_4_d,vdc_da_4_s]
            vdc_da_4=random.choice(list_vdc_da_4)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2,vdc_da_3,vdc_da_4]

            # Nội dung lời giải
            loigiai_vdc_1 = ('$SA$ và $BD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vdc_2 = ('$SB$ và $AC$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vdc_3 = ('$SC$ và $BD$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )
            loigiai_vdc_4 = ('$SD$ và $AC$ không cùng nằm trên một mặt phẳng và không có điểm chung nên hai đường thẳng chéo nhau.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2,loigiai_vdc_3,loigiai_vdc_4]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'+str(hinhve)+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

