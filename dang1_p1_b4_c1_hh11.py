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


def bt_dang1_p1_b4_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            hinhve=(
            '\\begin{center}  \n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]  \n'
                    '\\clip(-0.799081322049515,-0.7687016199356955) rectangle (6.89107985436939,3.771009458604631); \n'
                    '\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (3.,1.); \n'
                    '\\draw [dash pattern=on 1pt off 1pt] (3.,1.)-- (6.,1.); \n'
                    '\\draw (6.,1.)-- (3.,0.); \n'
                    '\\draw (3.,0.)-- (0.,0.); \n'
                    '\\draw [dash pattern=on 1pt off 1pt] (3.,1.)-- (1.,3.); \n'
                    '\\draw (6.,1.)-- (4.,3.); \n'
                    '\\draw (1.,3.)-- (4.,3.); \n'
                    '\\draw [dash pattern=on 1pt off 1pt] (4.390579745615408,1.)-- (2.4607594042276313,3.); \n'
                    '\\draw [dash pattern=on 1pt off 1pt] (4.390579745615408,1.)-- (1.5309390628398547,0.); \n'
                    '\\draw (1.,3.)-- (0.,0.); \n'
                    '\\draw (2.4607594042276313,3.)-- (1.5309390628398547,0.); \n'
                    '\\draw (4.,3.)-- (3.,0.); \n'
                    '\\draw (2.2,1.3862937595159774) node[anchor=north west] {$A$}; \n'
                    '\\draw (6.070650141380176,1.2769031311174155) node[anchor=north west] {$B$}; \n'
                    '\\draw (3.992228201807499,3.5522282018075066) node[anchor=north west] {$C$}; \n'
                    '\\draw (0.7323874755303524,3.5522282018075066) node[anchor=north west] {$D$}; \n'
                    '\\draw (2.8655047293023106,0.05172809305352008) node[anchor=north west] {$E$}; \n'
                    '\\draw (-0.5,0.2267530984912194) node[anchor=north west] {$F$}; \n'
                    '\\draw (4.418851652561891,1.5285015764341081) node[anchor=north west] {$I$}; \n'
                    '\\draw (2.362307838668926,3.5959844531669316) node[anchor=north west] {$J$}; \n'
                    '\\draw (1.2355843661637376,0.04078903021366387) node[anchor=north west] {$K$}; \n'
                '\\end{tikzpicture}  \n'
            '\\end{center}  \n'
                    )
            if dang=='6':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(IJE)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $AD // IJ$ suy ra $AD // (IJE)$. \\\\ \n'
                    '\\hspace*{1cm} $AK // IE$ suy ra $AK // (IJE)$. \\\\ \n'
                    'Mà $AD$ và $AK$ cắt nhau cùng nằm trên $(ADK)$ suy ra $(ADK) // (IJE)$.'
                        ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(ADK)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]
            if dang=='5':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(BJE)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $DI // BJ$ suy ra $DI // (BJE)$. \\\\ \n'
                    '\\hspace*{1cm} $DK // JE$ suy ra $DK // (BJE)$. \\\\ \n'
                    'Mà $DI$ và $DK$ cắt nhau cùng nằm trên $(DIK)$ suy ra $(DIK) // (BJE)$.'
                        ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(DIK)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]
            if dang=='4':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(BJE)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $DI // BJ$ suy ra $DI // (BJE)$. \\\\ \n'
                    '\\hspace*{1cm} $DK // JE$ suy ra $DK // (BJE)$. \\\\ \n'
                    'Mà $DI$ và $DK$ cắt nhau cùng nằm trên $(DIK)$ suy ra $(DIK) // (BJE)$.'
                        ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(DIK)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]
            if dang=='3':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ADF)$',
                    '$(BCE)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $IK // AF$ suy ra $IK // (ADF)$. \\\\ \n'
                    '\\hspace*{1cm} $IJ // AD$ suy ra $IJ // (ADF)$. \\\\ \n'
                    'Mà $IK$ và $IJ$ cắt nhau cùng nằm trên $(IJK)$ suy ra $(IJK) // (ADF)$.'
                        ),
                    ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $IK // BE$ suy ra $IK // (BCE)$. \\\\ \n'
                            '\\hspace*{1cm} $IJ // BC$ suy ra $IJ // (BCE)$. \\\\ \n'
                            'Mà $IK$ và $IJ$ cắt nhau cùng nằm trên $(IJK)$ suy ra $(IJK) // (BCE)$.'
                            ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(IJK)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]
            if dang=='2':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(ADF)$',
                    '$(IJK)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $BE // AF$ suy ra $BE // (ADF)$. \\\\ \n'
                    '\\hspace*{1cm} $BC // AD$ suy ra $BC // (ADF)$. \\\\ \n'
                    'Mà $BE$ và $BC$ cắt nhau cùng nằm trên $(BCE)$ suy ra $(BCE) // (ADF)$.'
                        ),
                    ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $BE // IK$ suy ra $BE // (IJK)$. \\\\ \n'
                            '\\hspace*{1cm} $BC // IJ$ suy ra $BC // (IJK)$. \\\\ \n'
                            'Mà $BE$ và $BC$ cắt nhau cùng nằm trên $(BCE)$ suy ra $(BCE) // (IJK)$.'
                        ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(BCE)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$(BCE)$',
                    '$(IJK)$',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Ta có \\\\ \n'
                    '\\hspace*{1cm} $AF // BE$ suy ra $AF // (BCE)$. \\\\ \n'
                    '\\hspace*{1cm} $AD // BC$ suy ra $AD // (BCE)$. \\\\ \n'
                    'Mà $AF$ và $AD$ cắt nhau cùng nằm trên $(ADF)$ suy ra $(ADF) // (BCE)$.'
                        ),
                    ('Ta có \\\\ \n'
                            '\\hspace*{1cm} $AF // IK$ suy ra $AF // (IJK)$. \\\\ \n'
                            '\\hspace*{1cm} $AD // IJ$ suy ra $AD // (IJK)$. \\\\ \n'
                            'Mà $AF$ và $AD$ cắt nhau cùng nằm trên $(ADF)$ suy ra $(ADF) // (IJK)$.'
                        ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$(AIJ)$',
                    '$(BIJ)$',
                    '$(ICE)$',
                    '$(IDF)$',
                    '$(ABCD)$',
                    '$(ABEF)$',
                    '$(CDFE)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('Cho hai hình bình hành $ABCD$ và $ABEF$ có chung cạnh $AB$ và không đồng phẳng. Gọi $I, J, K$ lần lượt là trung điểm của các cạnh $AB, CD, EF$. mặt phẳng $(ADF)$ song song với mặt phẳng nào sau đây? \n'
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+hinhve+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

