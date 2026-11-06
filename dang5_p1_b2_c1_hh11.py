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


def bt_dang5_p1_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(-9,9)
                #NHập đáp án đúng vào đây
                du = ['Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BF=\\frac{1}{4}BD$',
                    'Hình thang $MNEF$ với  $F$ là điểm trên cạnh $BD$ mà $EF//BC$.',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $FD=3BF$',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BD=4BF$',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BF=\\frac{1}{3}FD$',

                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('Xét hai mặt phẳng $(MNE)$ và $(BCD)$. Có $E\\in(MNE)\\cap (BCD)$.\\\\ \n'
                    'Và $MN//BC$ ($MN$ là đường trung bình của $\\Delta ABC$), $MN\\subset (MNE)$, $BC\\subset (BCD)$.\\\\ \n'
                    'Nên $(MNE)\\cap (BCD)=EF$ $( EF//MN/BC$ $F=BD\\cap EF)$.\\\\ \n'
                    'Do đó thiết diện tạo bởi mặt phẳng $(MNE)$ và tứ diện $(ABCD)$ là hình thang $MNEF$ ($MF//EF$).\\\\ \n'
                    'Hay $EF//CB$. Trong tam giác $DBC$ có $F\\in BD$ và $ED=3EC$ nên $FD=3BF$ vậy $BF=\\frac{1}{4}BD$.\n'
                    ),

                    ('Xét hai mặt phẳng $(MNE)$ và $(BCD)$. Có $E\\in(MNE)\\cap (BCD)$.\\\\ \n'
                            'Và $MN//BC$ ($MN$ là đường trung bình của $\\Delta ABC$), $MN\\subset (MNE)$, $BC\\subset (BCD)$\\\\ \n'
                            'Nên $(MNE)\\cap (BCD)=EF$ $( EF//MN/BC$ $F=BD\\cap EF)$.\\\\ \n'
                            'Do đó thiết diện tạo bởi mặt phẳng $(MNE)$ và tứ diện $(ABCD)$ là hình thang $MNEF$ ($MN//EF$).\\\\ \n'
                            'Vậy $EF//CB$.\n'
                            ),
                    ('Xét hai mặt phẳng $(MNE)$ và $(BCD)$. Có $E\\in(MNE)\\cap (BCD)$.\\\\ \n'
                            'Và $MN//BC$ ($MN$ là đường trung bình của $\\Delta ABC$), $MN\\subset (MNE)$, $BC\\subset (BCD)$.\\\\ \n'
                            'Nên $(MNE)\\cap (BCD)=EF$ $( EF//MN/BC$ $F=BD\\cap EF)$.\\\\ \n'
                            'Do đó thiết diện tạo bởi mặt phẳng $(MNE)$ và tứ diện $(ABCD)$ là hình thang $MNEF$ ($MF//EF$).\\\\ \n'
                            'Hay $EF//CB$. Trong tam giác $DBC$ có $F\\in BD$ và $ED=3EC$ vậy $FD=3BF$.\n'
                            ),

                    ('Xét hai mặt phẳng $(MNE)$ và $(BCD)$. Có $E\\in(MNE)\\cap (BCD)$.\\\\ \n'
                            'Và $MN//BC$ ($MN$ là đường trung bình của $\\Delta ABC$), $MN\\subset (MNE)$, $BC\\subset (BCD)$.\\\\ \n'
                            'Nên $(MNE)\\cap (BCD)=EF$ $( EF//MN/BC$ $F=BD\\cap EF)$.\\\\ \n'
                            'Do đó thiết diện tạo bởi mặt phẳng $(MNE)$ và tứ diện $(ABCD)$ là hình thang $MNEF$ ($MF//EF$).\\\\ \n'
                            'Hay $EF//CB$. Trong tam giác $DBC$ có $F\\in BD$ và $ED=3EC$ nên $FD=3BF$ vậy $BD=4BF$.\n'
                            ),

                    ('Xét hai mặt phẳng $(MNE)$ và $(BCD)$. Có $E\\in(MNE)\\cap (BCD)$.\\\\ \n'
                            'Và $MN//BC$ ($MN$ là đường trung bình của $\\Delta ABC$), $MN\\subset (MNE)$, $BC\\subset (BCD)$.\\\\ \n'
                            'Nên $(MNE)\\cap (BCD)=EF$ $( EF//MN/BC$ $F=BD\\cap EF)$.\\\\ \n'
                            'Do đó thiết diện tạo bởi mặt phẳng $(MNE)$ và tứ diện $(ABCD)$ là hình thang $MNEF$ ($MF//EF$).\\\\ \n'
                            'Hay $EF//CB$. Trong tam giác $DBC$ có $F\\in BD$ và $ED=3EC$ nên $FD=3BF$ vậy $BF=\\frac{1}{3}FD$.\n'
                            ),
                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BF=\\frac{1}{2}BD$',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $FD=4BF$',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BD=3BF$',
                    'Hình thang $MNEF$ với $F$ là điểm trên cạnh $BD$ mà $BF=\\frac{2}{3}FD$',
                    'Tứ giác $MNEF$ với $F$ là điểm bất kì trên cạnh $BD$',
                    'Tam giác $MNB$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                hinhve = ('\\begin{center} \n'
                    '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]\n'
            '\\clip(-1.3439669421487608,-2.5575657400450797) rectangle (4.997129977460552,3.7384522915101397);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);\n'
            '\\draw (0.,0.)-- (1.,-2.);\n'
            '\\draw (1.,-2.)-- (4.,0.);\n'
            '\\draw (2.,3.)-- (0.,0.);\n'
            '\\draw (2.,3.)-- (1.,-2.);\n'
            '\\draw (2.,3.)-- (4.,0.);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,0.)-- (1.75,-1.5);\n'
            '\\draw (1.,1.5)-- (1.5,0.5);\n'
            '\\draw (1.5,0.5)-- (1.75,-1.5);\n'
            '\\draw [dash pattern=on 2pt off 2pt] (1.,1.5)-- (1.,0.);\n'
            '\\draw (1.8566341096919585,3.7384522915101397) node[anchor=north west] {$A$};\n'
            '\\draw (-0.5,0.5228249436513878) node[anchor=north west] {$B$};\n'
            '\\draw (4,0.5077986476333562) node[anchor=north west] {$D$};\n'
            '\\draw (0.7446882043576241,-2) node[anchor=north west] {$C$};\n'
            '\\draw (1.5561081893313276,-1.5) node[anchor=north west] {$E$};\n'
            '\\draw (1.6462659654395169,0.883456048084145) node[anchor=north west] {$N$};\n'
            '\\draw (0.6094515401953402,2.115612321562732) node[anchor=north west] {$M$};\n'
            '\\draw (0.5,0) node[anchor=north west] {$F$};\n'
            '\\end{tikzpicture}\n'
            '\\end{center} \n'
            )

                # Câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M,N$ lần lượt là trung điểm của $AB$ và $AC$. '
                                '$E$ là điểm trên cạnh $CD$ và $ED=3EC$. Thiết diện tạo bởi mặt phẳng $(MNE)$'
                                ' và tứ diện $ABCD$ là'
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

