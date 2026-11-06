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


def bt_dang1_p2_b5_c1_hh11(self):
            # Khai báo biến

            # Nội dung câu hỏi
            noidungcauhoi = 'Cho hình hộp $ABCD.A\'B\'C\'D\'$. $M, N$ là trung điểm cạnh $AB$ và $CD$. \n'

            hinhve = (   
                    '\\begin{center}  \n'
                    '\\scalebox{0.6}{'  
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]  \n'
                        '\\clip(-1.074895358774673,-0.7445060406609769) rectangle (8.292231511219146,8.055734188785662); \n'
                        '\\draw (0.,0.)-- (4.,0.); \n'
                        '\\draw (4.,0.)-- (6.,2.); \n'
                        '\\draw [dash pattern=on 3pt off 3pt] (6.,2.)-- (2.,2.); \n'
                        '\\draw [dash pattern=on 3pt off 3pt] (2.,2.)-- (0.,0.); \n'
                        '\\draw (1.,5.)-- (0.,0.); \n'
                        '\\draw [dash pattern=on 3pt off 3pt] (2.,2.)-- (3.,7.); \n'
                        '\\draw (4.,0.)-- (5.,5.); \n'
                        '\\draw (6.,2.)-- (7.,7.); \n'
                        '\\draw (7.,7.)-- (3.,7.); \n'
                        '\\draw (3.,7.)-- (1.,5.); \n'
                        '\\draw (1.,5.)-- (5.,5.); \n'
                        '\\draw (5.,5.)-- (7.,7.); \n'
                        '\\draw [dash pattern=on 3pt off 3pt] (1.,1.)-- (5.,1.); \n'
                        '\\draw (1.435602620791394,2.737797608414534) node[anchor=north west] {$A$}; \n'
                        '\\draw (-0.6024898249853593,0.4027645413987843) node[anchor=north west] {$B$}; \n'
                        '\\draw (3.932603299392052,0.21380232788305895) node[anchor=north west] {$C$}; \n'
                        '\\draw (6.065176851926668,2.4408569871755366) node[anchor=north west] {$D$}; \n'
                        '\\draw (0.3693158445240859,1.6310189292509993) node[anchor=north west] {$M$}; \n'
                        '\\draw (5.079873881451814,1.428559414769865) node[anchor=north west] {$N$}; \n'
                        '\\draw (2.420905591266248,7.6643124607888025) node[anchor=north west] {$A\'$}; \n'
                        '\\draw (0.28833203873163216,5.518241607288779) node[anchor=north west] {$B\'$}; \n'
                        '\\draw (5.012387376624768,5.329279393773053) node[anchor=north west] {$C\'$}; \n'
                        '\\draw (7.009987919505295,7.529339451134713) node[anchor=north west] {$D\'$}; \n'
                    '\\end{tikzpicture} } \n'
                '\\end{center}  \n'

                )

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Ảnh của điểm $A\'$ qua phép chiếu song song theo phương $CC\'$ trên mặt phẳng $(ABCD)$ là điểm $A$'
            nb_da_1_s = 'Ảnh của điểm $A\'$ qua phép chiếu song song theo phương $CC\'$ trên mặt phẳng $(ABCD)$ là điểm $B$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Ảnh của điểm $B$ qua phép chiếu song song theo phương $C\'D\'$ trên mặt phẳng $(ADD\'A\')$ là điểm $A$'
            nb_da_2_s = 'Ảnh của điểm $B$ qua phép chiếu song song theo phương $C\'D\'$ trên mặt phẳng $(ADD\'A\')$ là điểm $D$'
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]
            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1,nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Ảnh của điểm $A\'$ qua phép chiếu song song theo phương $CC\'$ trên mặt phẳng $(ABCD)$ là điểm $A$.'
                        )
            loigiai_nb_2 = ('Ảnh của điểm $B$ qua phép chiếu song song theo phương $C\'D\'$ trên mặt phẳng $(ADD\'A\')$ là điểm $A$  .'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Ảnh của điểm $D\'$ qua phép chiếu song song theo phương $MA\'$ trên mặt phẳng $(ABCD)$ là điểm $N$'
            th_da_1_s = 'Ảnh của điểm $D\'$ qua phép chiếu song song theo phương $MA\'$ trên mặt phẳng $(ABCD)$ là trung điểm của $AD$'
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ảnh của điểm $D\'$ qua phép chiếu song song theo phương $MA\'$ trên mặt phẳng $(ABCD)$ là điểm $N$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Ảnh của đoạn thẳng $B\'C\'$ qua phép chiếu song song theo phương $MB\'$ trên mặt phẳng $(ABCD)$ là đoạn thẳng $MN$'
            vd_da_1_s = 'Ảnh của đoạn thẳng $B\'C\'$ qua phép chiếu song song theo phương $MB\'$ trên mặt phẳng $(ABCD)$ là đoạn thẳng $AD$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Ảnh của đoạn thẳng $B\'C\'$ qua phép chiếu song song theo phương $MB\'$ trên mặt phẳng $(ABCD)$ là đoạn thẳng $MN$.'
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True $S$ là diện tích hình chiếu của tam giác $A\'B\'C\'$ qua phép chiếu song song theo phương $AA\'$. $S=\\dfrac{1}{2} S_{\\Delta ABCD}$'
            vdc_da_1_s = '$S$ là diện tích hình chiếu của tam giác $A\'B\'C\'$ qua phép chiếu song song theo phương $AA\'$. $S=\\dfrac{1}{3} S_{\\Delta ABCD}$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Qua phép chiếu song song theo phương $AA\'$ \\\\ \n'
                            '\\hspace*{1cm} Tam giác $A\'B\'C\'$ biến thành tam giác $ABC$ có diện tích là $S$. \\\\ \n'
                            '\\hspace*{1cm} $S=\\dfrac{1}{2} S_{\\Delta ABCD}$.'

                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

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
                '\\loigiai{ \n'+hinhve+
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

