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


def bt_dang4_p1_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['$RT$ song song $MQ$',
                      '$RT$ song song $AD$',
                      '$MQ$ song song $AD$',
                      '$NP$ song song $DC$',
                      '$PQ$ song song $BD$',


                      ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Xét $\\Delta SAD$ có $RT$ là đường trung bình của tam giác $\\Rightarrow RT//AD$ $(1)$.\\\\ \n'
                       'Xét $\\Delta CAD$ có $MQ$ là đường trung bình của tam giác $\\Rightarrow MQ//AD$ $(2)$. \\\\ \n'
                       'Từ $(1)$ và $(2)$ $\\Rightarrow RT//MQ$.\n'
                       ),

                      ('Xét $\\Delta SAD$ có $RT$ là đường trung bình của tam giác $\\Rightarrow RT//AD$.\\\\ \n'
                            ),
                      ('Xét $\\Delta CAD$ có $MQ$ là đường trung bình của tam giác $\\Rightarrow MQ//AD$.\\\\ \n'
                            ),

                      ('Xét $\\Delta BDC$ có $NP$ là đường trung bình của tam giác $\\Rightarrow NP//DC$.\\\\ \n'
                            ),

                      ('Xét $\\Delta CBD$ có $PQ$ là đường trung bình của tam giác $\\Rightarrow PQ//BD$.\\\\ \n'
                            ),
                      ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['$RT$ song song $BC$',
                      '$RT$ song song $NP$',
                      '$NP$ song song $MQ$',
                      '$MQ$ song song $SD$',
                      '$PQ$ song song $RT$',
                      '$RP$ song song $MQ$',
                      '$TQ$ song song $RP$',
                      '$TP$ song song $RN$',
                      '$RP$ song song $MN$',
                      '$TN$ song song $RP$',
                      '$RQ$ song song $MN$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.3146692268130882,-2.6583516848860844) rectangle (5.121016651381502,3.644365476816884);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);\n'
            '\\draw (1.,-2.)-- (3.578579540078666,-1.993508102427967);\n'
            '\\draw (4.,0.)-- (3.578579540078666,-1.993508102427967);\n'
            '\\draw (1.,-2.)-- (0.,0.);\n'
            '\\draw (2.,3.)-- (0.,0.);\n'
            '\\draw (1.,-2.)-- (2.,3.);\n'
            '\\draw (2.,3.)-- (4.,0.);\n'
            '\\draw (3.578579540078666,-1.993508102427967)-- (2.,3.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (3.578579540078666,-1.993508102427967);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,-2.)-- (4.,0.);\n'
            '\\draw (1.,1.5)-- (1.5,0.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.789289770039333,-0.9967540512139835)-- (2.289289770039333,-1.9967540512139834);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (2.289289770039333,-1.9967540512139834)-- (3.789289770039333,-0.9967540512139835);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (3.789289770039333,-0.9967540512139835)-- (2.5,-1.);\n'
            '\\draw (1.5,0.5)-- (2.289289770039333,-1.9967540512139834);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,1.5)-- (1.789289770039333,-0.9967540512139835);\n'
            '\\draw (1.8499862256875574,3.617771733518559) node[anchor=north west] {$S$};\n'
            '\\draw (-0.6,0.2270694629821521) node[anchor=north west] {$A$};\n'
            '\\draw (0.5,-1.913726872532991) node[anchor=north west] {$D$};\n'
            '\\draw (3.578579540078666,-1.8339456426380167) node[anchor=north west] {$C$};\n'
            '\\draw (3.9774856895535375,0.29355382122796403) node[anchor=north west] {$B$};\n'
            '\\draw (2.1558142736182924,-0.39788350452847976) node[anchor=north west] {$N$};\n'
            '\\draw (3.8,-0.7037115524592145) node[anchor=north west] {$P$};\n'
            '\\draw (0.5,2.022147135619073) node[anchor=north west] {$R$};\n'
            '\\draw (1.6106425360026346,0.8919130454402711) node[anchor=north west] {$T$};\n'
            '\\draw (2.1425174019691298,-1.9403206158313158) node[anchor=north west] {$Q$};\n'
            '\\draw (1.2,-0.7834927823541888) node[anchor=north west] {$M$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABCD$. Gọi $M,N,P,Q,R,T$ lần lượt là trung điểm của các cạnh $AC,BD,BC,CD,SA,SD$.'
                                 ' Cặp đường thẳng nào sau đây song song với nhau? \\\\ \n'
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

