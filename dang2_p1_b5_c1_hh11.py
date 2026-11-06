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


def bt_dang2_p1_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',



                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Gọi $N$ là trung điểm $SC$.'
                    ' Khi đó $MN//AC$ nên hình chiếu của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$.'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.903125561147522,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (0.9,2) node[anchor=north west] {$A$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (1.2,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw (3,2.8364274330082737) node[anchor=north west] {$N$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (3.,2.5);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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
                du = [
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SB$',



                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [

                    ('Gọi $N$ là trung điểm $SB$.'
                    ' Khi đó $MN//AB$ nên hình chiếu của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SB$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.8,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (0.95,1.908687375143544) node[anchor=north west] {$A$};\n'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (3.782393883488894,3.7522733875670458) node[anchor=north west] {$N$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};'
            '\\draw (1.23,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (3.75,3.25);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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
                du = [
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',



                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [          
                    ('Gọi $N$ là trung điểm $SD$.'
                    ' Khi đó $MN//AD$ nên hình chiếu của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.8,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (0.95,1.908687375143544) node[anchor=north west] {$A$};\n'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};'
            '\\draw (1.23,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw (0.5,2.884003846232106) node[anchor=north west] {$N$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (1.,2.5);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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
                du = [
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $O$',



                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [          
                    ('Ta có $O$ là trung điểm $AC$.'
                    ' Khi đó $MO//SC$ nên hình chiếu của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $O$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.8,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (0.95,1.908687375143544) node[anchor=north west] {$A$};\n'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (1.23,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (2.75,0.75);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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
                du = [
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',



                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [

                    ('Gọi $N$ là trung điểm $AB$.'
                    ' Khi đó $MN//SB$ nên hình chiếu của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$.'),


                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.903125561147522,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (0.9,2) node[anchor=north west] {$A$};\n'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};'
            '\\draw (1.2,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw (3.4493589909220685,2.0038402015912085) node[anchor=north west] {$N$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (3.5,1.5);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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

            if dang=='6':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',


                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [
                    ('Gọi $N$ là trung điểm $AD$.'
                    ' Khi đó $MN//SD$ nên hình chiếu của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$.'),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SB$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $A$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AD$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AB$',

                    'Hình chiếu song song của điểm $M$ theo phương $AC$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AB$ lên mặt phẳng $(SBC)$ là điểm trung điểm $SD$',
                    'Hình chiếu song song của điểm $M$ theo phương $AD$ lên mặt phẳng $(SCD)$ là điểm trung điểm $SC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SC$ lên mặt phẳng $(ABCD)$ là điểm $C$',
                    'Hình chiếu song song của điểm $M$ theo phương $SB$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    'Hình chiếu song song của điểm $M$ theo phương $SD$ lên mặt phẳng $(ABCD)$ là điểm trung điểm $AC$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.2607059182373204,-0.6604389389434) rectangle (7.433883598418016,5.595859399990547);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw (4.,0.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (5.5,1.5)-- (1.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (0.,0.);\n'
            '\\draw (0.,0.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.,5.)-- (1.5,1.5);\n'
            '\\draw (2.,5.)-- (0.,0.);\n'
            '\\draw (2.,5.)-- (4.,0.);\n'
            '\\draw (2.,5.)-- (5.5,1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.5,1.5);\n'
            '\\draw (1.903125561147522,5.548282986766715) node[anchor=north west] {$S$};\n'
            '\\draw (1.5,2) node[anchor=north west] {$A$};\n'
            '\\draw (-0.55,0.16025418916770712) node[anchor=north west] {$D$};\n'
            '\\draw (3.996487742996139,0.14836008586174904) node[anchor=north west] {$C$};\n'
            '\\draw (5.649768102524309,1.7540640321660892) node[anchor=north west] {$B$};\n'
            '\\draw (1.2,3.692802871037255) node[anchor=north west] {$M$};\n'
            '\\draw (2.485936623139467,0.7668534577715689) node[anchor=north west] {$O$};'
            '\\draw (0.3,1.266405796621808) node[anchor=north west] {$N$};\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.75,3.25)-- (0.75,0.75);\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$, $M,N,P,Q$ lần lượt là trung điểm cạnh $SA,SB,SC,SD$. Mệnh đề nào sau đây đúng? \n'
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
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

