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


def bt_dang21_p1_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                a=randint(20,50)
                b=randint(20,50)
                while a-5<=b:
                    a=randint(20,50)
                    b=randint(20,50)
                listen=['Chiến','Hùng','Bình','Việt','Nam','Cường','Hưng','Kha','Sơn','Lâm','Hoàng']
                ten=random.choice(listen)

                # Câu hỏi
                noidungcauhoi = ('Ông %s có một mảnh vườn hình Elip có chiều dài trục lớn và trục nhỏ lần lượt là $%s $m và $%s $m.'
                                ' Ông chia mảnh vườn ra làm hai nửa bằng một đường tròn tiếp xúc trong với Elip để làm mục đích sử dụng khác nhau (xem hình vẽ).'
                                ' Nửa bên trong đường tròn ông trồng cây lâu năm, nửa bên ngoài đường tròn ông trồng hoa màu. '
                                ' Biết diện tích hình Elip được tính theo công thức $S=\\pi ab$ ,'
                                ' với $a, b$ lần lượt là nửa độ dài trục lớn và nửa độ dài trục nhỏ, và độ rộng của đường Elip là không đáng kể. Khi đó diện tích trồng hoa màu là'
                                '\\begin{center}'
                                '''\\scalebox{0.7}{
                                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-5.12759898579725,-2) rectangle (4.4907298366906785,2);
                \\draw [rotate around={0.:(0.,0.)}] (0.,0.) ellipse (3.6055512754639882cm and 2.cm);
                \\draw(0.,0.) circle (2.cm);
                \\draw (-0.4995,0.9) node[anchor=north west] {\\parbox{1 cm}{Trồng cây lâu năm}};
                \\draw (2,0.9) node[anchor=north west] {\\parbox{1.2762271967832046 cm}{Trồng hoa màu}};
                \\draw (-3.2,0.9) node[anchor=north west] {\\parbox{1.2762271967832046 cm}{Trồng hoa màu}};
            \\end{tikzpicture}}'''
            '\\end{center}'
                                %(str(ten),latex(a),latex(b)))

                # Nội dung lời giải
                loigiai=('Theo đề ta có $a=%s,b=%s$ nên diện tích Elip là $$S_{(E)}=\\pi\\cdot a\\cdot b=\\pi\\cdot %s\\cdot %s=%s \\pi \\text{     (m)$^2$}.$$'
                        'Vì đường tròn tiếp xúc trong, nên sẽ tiếp xúc tại đỉnh của trục nhỏ, suy ra bán kính đường tròn là '
                        '$R=b=%s $ (m), nên diện tích hình tròn $(C)$ trồng cây lâu năm là'
                        ' $$S_{(C)}=\\pi \\cdot R^2=\\pi \\cdot \\left(%s\\right)^2=%s\\pi \\text{     (m)$^2$}.$$'
                        'Khi đó diện tích trồng hoa màu là $S=S_{(E)}-S_{(C)}=%s\\pi-%s\\pi=%s\\pi \\text{     m$^2$}$.'
                        %(latex(Rational(a,2)),latex(Rational(b,2)),latex(Rational(a,2)),latex(Rational(b,2)),latex(Rational(a*b,4)),
                        latex(Rational(b,2)),latex(Rational(b,2)),latex(Rational(b**2,4)),
                        latex(Rational(a*b,4)),latex(Rational(b**2,4)),latex(Rational(a*b,4)-Rational(b**2,4)),

                        ))

                du = ['$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b,4)-Rational(b**2,4))),

                    ]
                da= random.choice(du)
                s = ['$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b+8,4)-Rational(b**2,4))),
                    '$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b,4)-Rational(b**2-8,4))),
                    '$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b+2,4)-Rational(b**2,4))),
                    '$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b,4)-Rational(b**2-2,4))),
                    '$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b+4,4)-Rational(b**2,4))),
                    '$%s\\pi \\text{     m$^2$}$'%(latex(Rational(a*b,4)-Rational(b**2-4,4))),

                    ]
                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Các đáp án
                da_d = ('\\True ' +str(da))     
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('frac','dfrac').replace('+-', '-').replace('-+', '-').replace('--', '+').replace('++', '+')
            return content

