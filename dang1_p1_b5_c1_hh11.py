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


def bt_dang1_p1_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            # Khai báo biến 
            if dang=='8':

                du = ['đường thẳng đi qua $A$ hoặc chính là $A$',
                    ]
                da= random.choice(du)
                s = ['điểm $A$',
                    'trùng với phương chiếu',
                    'đường thẳng đi qua $A$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Nếu đường thẳng $a$ cắt mặt phẳng chiếu $(P)$ tại điểm $A$ thì hình chiếu của $a$ sẽ là'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Nếu phương chiếu song song hoặc trùng với đường thẳng $a$ thì hình chiếu là điểm $A$. \\\\ \n'
                        'Nếu phương chiếu không song song hoặc không trùng với đường thẳng $a$ thì hình chiếu là đường thẳng đi qua điểm $A$.'
                        )  
            if dang=='7':

                du = ['Một đường thẳng luôn cắt hình chiếu của nó',
                    ]
                da= random.choice(du)
                s = ['Một tam giác bất kỳ đề có thể xem là hình biểu diễn của một tam giác cân',
                    'Một đường thẳng có thể song song với hình chiếu của nó',
                    'Hình chiếu song song của hai đường thẳng chéo nhau có thể song song với nhau',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong các mện đề sau mệnh đề nào \\textbf{sai}?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Khi mặt phẳng chiếu song song với đường thẳng đã cho thì đường thẳng đó song song với hình chiếu của nó.'
                        ) 
            if dang=='6':

                du = ['Hình thang',
                    ]
                da= random.choice(du)
                s = ['Hình vuông',
                    'Hình bình hành',
                    'Hình thoi',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Hình chiếu của hình vuông không thể là hình nào trong các hình sau?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tính chất của phép chiếu song song.'
                        ) 
            if dang=='5':

                du = ['ba đường thẳng đôi một song song với nhau',
                    ]
                da= random.choice(du)
                s = ['ba đường thẳng cắt nhau',
                    'một điểm',
                    'ba đường thẳng chéo nhau',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Qua phép chiếu song song biến ba đường thẳng song song thành'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Hình chiếu song song của ba đường thẳng song song thành ba đường thẳng đôi một song song với nhau.'
                        ) 
            if dang=='4':

                du = ['Hình chiếu song song của hai đường thẳng chéo nhau có thể trùng nhau',
                    ]
                da= random.choice(du)
                s = ['Hình chiếu song song của hai đường thẳng chéo nhau có thể song song với nhau',
                    'Một đường thẳng có thể trùng với hình chiếu của nó',
                    'Một tam giác bất kỳ đều có thể xem là hình biểu diễn của một tam giác cân',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong các mệnh đề sau mệnh đề nào \\textbf{sai}?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Hình chiếu song song của hai đường thẳng chéo nhau chỉ có thể song song hoặc cắt nhau.'
                        ) 
            if dang=='3':

                du = ['Hình chiếu song song của một hình chóp cụt có thể là một hình tam giác',
                    ]
                da= random.choice(du)
                s = ['Hình chiếu song song của một hình chóp cụt có thể là một đoạn thẳng',
                    'Hình chiếu song song của một hình chóp cụt có thể là một hình chóp cụt',
                    'Hình chiếu song song của một hình chóp cụt có thể là một điểm',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Khẳng định nào sau đây đúng?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Qua phép chiếu song song chỉ có thể biến hình chóp cụt thành một đa giác.'
                        ) 
            if dang=='2':

                du = ['Phép chiếu song song biến hai đường thẳng song song thành hai đường thẳng song song',
                    ]
                da= random.choice(du)
                s = ['Phép chiếu song song biến đường thẳng thành đường thẳng, biến tia thành tia, biến đoạn thẳng thảnh đoạn thẳng',
                    'Phép chiếu song song biến ba điểm thẳng hàng thành ba điểm thẳng hàng và không thay đổi thứ tự của ba điểm đó',
                    'Phép chiếu song song không làm thay đổi tỉ số độ dài của hai đoạn thẳng nằm trên hai đường thẳng song song hoặc cùng nằm trên một đường thẳng',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Trong các mệnh đề sau mệnh đề nào \\textbf{sai}?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Tính chất của phép chiếu song song. \\\\ \n'
                        'Phép chiếu song song biến hai đường thẳng song song thành hai đường thẳng song song hoặc trùng nhau.'
                        )
            if dang=='1':

                du = ['Chéo nhau',
                    ]
                da= random.choice(du)
                s = ['Đồng quy',
                    'Song song',
                    'Thẳng hàng',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Qua phép chiếu song song, tính chất nào không được bảo toàn?'
                                )
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('Do hai đường thẳng qua phép chiếu song song ảnh của chúng sẽ cùng thuộc một mặt phẳng. \\\\ \n'
                        'Suy ra tính chất chéo nhau không được bảo toàn.'
                        )

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

