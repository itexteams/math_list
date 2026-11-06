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


def bt_dang2_p3_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(1,9)
                b=randint(2,9)
                c=randint(2,9)
                pq=b*a*sqrt(2)/(2*b+2)+(a*sqrt(2))/(2*c)
                ao=(a*sqrt(2))/2
                s=ao*pq/2
                h1=ao*pq/2
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho hình chóp $S$zz$ABCD$ có đáy là hình vuông tâm $O$ cạnh $%s$$zz$ Trên cạnh $SB, SD$ lần lượt lấy điểm $M, N$ sao cho $SM = %sMB$ và $SN = \\frac{1}{%s}SD$$zz$ Diện tích hình chiếu song song của tam giác $AMN$ lên mặt phẳng $(ABCD)$ theo phương của đường thẳng $SO$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục) \n'
                                %(latex(a),latex(b),latex(c)
                                ))

                # Nội dung lời giải
                loigiai = (

                            '\\begin{center}  \n'
                                '\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1$zz$0cm,y=1$zz$0cm]  \n'
                                    '\\clip(-1$zz$102147117622518,-0$zz$5784768007983005) rectangle (6$zz$749119106770371,5$zz$861732360224431); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (2$zz$,2$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw (6$zz$,2$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw (4$zz$,0$zz$)-- (0$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (4$zz$07,1$zz$36); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$,0$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$,1$zz$)-- (2$zz$,5$zz$); \n'
                                    '\\draw (2$zz$,5$zz$)-- (0$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,5$zz$)-- (2$zz$,2$zz$); \n'
                                    '\\draw (2$zz$,5$zz$)-- (6$zz$,2$zz$); \n'
                                    '\\draw (2$zz$,5$zz$)-- (4$zz$,0$zz$); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (3$zz$3831096543171015,3$zz$9626677592621737)-- (4$zz$073526163541213,1$zz$3578420545137375); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$6790382242999946,1$zz$6975955607499866)-- (1$zz$066889190052508,0$zz$35562973001750264); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (0$zz$6790382242999946,1$zz$6975955607499866)-- (3$zz$3831096543171015,3$zz$9626677592621737); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (1$zz$066889190052508,0$zz$35562973001750264); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (0$zz$6790382242999946,1$zz$6975955607499866); \n'
                                    '\\draw [dash pattern=on 2pt off 2pt] (2$zz$,2$zz$)-- (3$zz$3831096543171015,3$zz$9626677592621737); \n'
                                    '\\draw (1$zz$7440876426796657,5$zz$6) node[anchor=north west] {S}; \n'
                                    '\\draw (1$zz$5631828909655439,2$zz$5) node[anchor=north west] {A}; \n'
                                    '\\draw (-0$zz$4991312785754451,0$zz$10896125571536185) node[anchor=north west] {B}; \n'
                                    '\\draw (3$zz$9,0) node[anchor=north west] {C}; \n'
                                    '\\draw (6$zz$037560416694824,2$zz$3) node[anchor=north west] {D}; \n'
                                    '\\draw (2$zz$6244907676883917,1) node[anchor=north west] {O}; \n'
                                    '\\draw (0$zz$1,2$zz$2) node[anchor=north west] {M}; \n'
                                    '\\draw (3$zz$2757478738592303,4$zz$6) node[anchor=north west] {N}; \n'
                                    '\\draw (1$zz$0325289526041197,0$zz$4) node[anchor=north west] {P}; \n'
                                    '\\draw (4$zz$0234875142776,1$zz$4) node[anchor=north west] {Q}; \n'
                                '\\end{tikzpicture}  \n'
                            '\\end{center}  \n'


                            'Trong $(SBD)$ vẽ $MP // SO \\Rightarrow P$ là hình chiếu song song của $M$ lên $(ABCD)$ theo phương $SO$$zz$ \\\\ \n'
                            'Trong $(SBD)$ vẽ $NQ // SO \\Rightarrow Q$ là hình chiếu song song của $N$ lên $(ABCD)$ theo phương $SO$$zz$ \\\\ \n'
                            '$\\Rightarrow$ Hình chiếu song song của tam giác $AMN$ lên mặt phẳng $(ABCD)$ theo phương của đường thẳng $SO$ là $APQ$$zz$ \\\\ \n'

                            'Vì $MP // SO \\Rightarrow \\frac{BM}{BS} = \\frac{BP}{BO}$$zz$ \\\\ \n'
                            'Mà $SM = %sMB \\Rightarrow BM = \\frac{1}{%s}BS \\Rightarrow \\frac{BM}{BS} = \\frac{1}{%s}$$zz$ \\\\ \n'
                            '\\hspace*{1cm} $\\Rightarrow \\frac{BP}{BO} = \\frac{1}{%s} \\Rightarrow OP = %sOB \\Rightarrow OP = %sBD = %s$ \\hspace*{1cm} (1)$zz$ \\\\ \n'

                            'Tương tự, ta có $NQ // SO \\Rightarrow \\frac{DN}{DS} = \\frac{DQ}{DO}$$zz$ \\\\ \n'
                            'Mà $SN = \\frac{1}{%s}SD \\Rightarrow ND = %sSD \\Rightarrow \\frac{ND}{SD} = %s$$zz$ \\\\ \n'
                            '\\hspace*{1cm} $\\Rightarrow \\frac{DQ}{DO} = %s \\Rightarrow DQ = %sDO \\Rightarrow OQ = \\frac{1}{%s}DO = %s BD = %s$ \\hspace*{1cm}  (2)$zz$ \\\\ \n'

                            'Từ (1) và (2) suy ra $PQ = OP + OQ = %s$$zz$\\\\ \n'
                            '\\hspace*{1cm} $\\Rightarrow S_{APQ} = \\frac{1}{2}AO \\cdot PQ = \\frac{1}{2} \\cdot %s \\cdot %s = %s$$zz$\\\\ \n'

                            'Vậy diện tích hình chiếu song song của tam giác $AMN$ lên mặt phẳng $(ABCD)$ theo phương của đường thẳng $SO$ là $%s$$zz$'

                        %(latex(b),latex(b+1),latex(b+1),
                            latex(b+1),latex(1-Rational(1,b+1)),latex(Rational(b,2*b+2)),latex(b*a*sqrt(2)/(2*b+2)),
                            latex(c),latex(1-Rational(1,c)),latex(1-Rational(1,c)),
                            latex(1-Rational(1,c)),latex(1-Rational(1,c)),latex(c),latex(Rational(1,2*c)),latex((a*sqrt(2))/(2*c)),
                            latex(b*a*sqrt(2)/(2*b+2)+(a*sqrt(2))/(2*c)),
                            latex(ao),latex(pq),latex(s),
                            latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                                

