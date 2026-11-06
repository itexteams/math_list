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


def bt_dang17_p1_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                ad=randint(2,9)
                ab=2*ad
                sa=randint(2,9)
                ai=ad
                while ad==sa:
                    ab=2*ad
                    sa=randint(2,9)
                    ai=ad

                si2=sa**2+ai**2 
                sd2=sa**2+ad**2 
                di=ai*sqrt(2)

                gtri=(sd2+di**2-si2)/(2*sqrt(sd2)*di)
                goc1=acos(gtri)
                gocz=goc1*180/pi

                h1=gocz
                number = Decimal(float(h1))  # Số cần làm tròn
                goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                du = ['$%s^\\circ$'%(latex(goc)),
                    ]
                da= random.choice(du)
                s = ['$%s^\\circ$'%(latex(goc+1)),
                    '$%s^\\circ$'%(latex(goc+2)),
                    '$%s^\\circ$'%(latex(goc+3)),
                    '$%s^\\circ$'%(latex(goc-1)),
                    '$%s^\\circ$'%(latex(goc-2)),
                    '$%s^\\circ$'%(latex(goc-3)),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''                     
                                Cho hình chóp $SzzABCD$ có đáy là hình thang vuông tại $A$ và $D$, $AD=DC=%s a$, $AB=%s a$, $SA$ vuông góc với $AB$ và $AD$, $SA=%s a$zz Góc giữa hai đường thẳng $SD$ và $BC$ là
                                '''
                                %(latex(ad),latex(ab),latex(sa)
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
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-2zz87311370593609,-2zz673694572998763) rectangle (6zz84732369216414,3zz821528573197235);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (-2zz,-2zz);
                    \\draw [line width=1zzpt] (-2zz,-2zz)-- (1zz,-2zz);
                    \\draw [line width=1zzpt] (1zz,-2zz)-- (6zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (6zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (1zz,-2zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (0zz,3zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (-2zz,-2zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (1zz,-2zz);
                    \\draw [line width=1zzpt] (0zz,3zz)-- (6zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,3zz)-- (3zz,0zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (3zz,0zz)-- (1zz,-2zz);
                    \\draw (-0zz23022980507012897,3zz7) node[anchor=north west] {$S$};
                    \\draw (-0zz6,0zz5216565839804177) node[anchor=north west] {$A$};
                    \\draw (-2zz6,-1zz7778017252475906) node[anchor=north west] {$B$};
                    \\draw (0zz9,-1zz8524594625601882) node[anchor=north west] {$C$};
                    \\draw (6zz055951676650603,0zz38727265681774187) node[anchor=north west] {$D$};
                    \\draw (2zz9949844468340947,0zz7008351535306521) node[anchor=north west] {$I$};
                \\end{tikzpicture}
            \\end{center}            
                    Gọi $I$ là trung điểm của $AB$, khi đó $AI=%s a$zz Tứ giác $ADCI$ là hình hình hành (do $AI//DC$), có $AI=AD=%s a$ nên là hình thoizz Lại có góc $A$, $D$ vuông nên $ADCI$ là hình vuông cạnh $a$ suy ra $DI=%s a\\sqrt{2}$zz\\\\
                    Mặt khác, tứ giác $BIDC$ là hình hình hành (do cặp cạnh $DC$ và $BI$ song song và bằng nhau) nên $BC//DI$zz Khi đó, $\\left(SD,BC\\right)=\\left(SD,DI\\right)$zz\\\\
                    Tam giác $SAI$ vuông tại $A$ nên $SI^2=SA^2+AI^2=%s a^2+%s a^2=%s a^2$zz\\\\
                    Tam giác $SAD$ vuông tại $A$ nên $SD^2=SA^2+AD^2=%s a^2+%s a^2=%s a^2$zz\\\\
                    Áp dụng định lý hàm số cosin trong tam giác $SDI$ ta được \\\\
                    $\\cos \\widehat{SDI}=\\dfrac{SD^2+DI^2-SI^2}{2\\cdot SD \\cdot DI}=\\dfrac{%s a^2+%s a^2-%s a^2}{2 \\cdot %s a \\cdot %s a}=%s$zz \\\\
                    Do $\\cos \\widehat{SDI} >0$ nên góc $SDI$ là góc nhọn suy ra $\\alpha=\\widehat{SDI}=%s^\\circ$zz'''
                        %(latex(ai),latex(ai),latex(ai),
                        latex(sa**2),latex(ai**2),latex(si2),
                        latex(sa**2),latex(ad**2),latex(sd2),
                        latex(sd2),latex(di**2),latex(si2),latex(sqrt(sa**2+ad**2 )),latex(di),latex(gtri),
                        latex(goc)
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content

