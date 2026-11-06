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


def bt_dang1_p3_b2_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3','4']
            dang=random.choice(lisdang)
            if dang=='4':
                a=randint(2,9)
                h1=1/(a+1)   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Lấy điểm $M$ thuộc cạnh $BC$ sao cho $MC = %sMB$. Gọi $N, P$ lần lượt là trung điểm của $BD$ và $AD$. Gọi $Q$ là giao điểm của $AC$ với mặt phẳng $(MNP)$. Tỉ số giữa $AQ$ và $AC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                                    '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8846639380149807,-2.93800878259941) rectangle (6.889799016271905,4.902902573006158); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (2.,-2.)-- (6.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,0.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (6.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (5.,4.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (2.5,2.)-- (3.5,1.); \n'
                                '\\draw [line width=1.pt] (3.5,1.)-- (3.368,-1.316); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.368,-1.316)-- (1.84,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.84,0.)-- (2.5,2.); \n'
                                '\\draw (-0.47268384983909434,0.2) node[anchor=north west] {A}; \n'
                                '\\draw (1.826430835787626,-2) node[anchor=north west] {B}; \n'
                                '\\draw (6,0.2) node[anchor=north west] {C}; \n'
                                '\\draw (5,4.5) node[anchor=north west] {D}; \n'
                                '\\draw (3.381323426645003,-1.3) node[anchor=north west] {M}; \n'
                                '\\draw (3.4,1.2) node[anchor=north west] {N}; \n'
                                '\\draw (2.1586728423810824,2.6) node[anchor=north west] {P}; \n'
                                '\\draw (1.3,0.6) node[anchor=north west] {Q}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                        'Từ giả thiết suy ra $PN // AB$. \\\\ \n'
                        'Chọn mặt phẳng phụ $(ABC)$ chứa $AC$. \\\\ \n'
                        'Hai mặt phẳng $(ABC)$ và $(MNP)$ có điểm chung $M$ và lần lượt chứa hai đường thẳng song song là $AB$, $PN$ nên giao tuyến của chúng là đường thẳng $d$ đi qua $M$ và song song với $PN$, $AB$. Trong mặt phẳng $(ABC)$, $d \\cap AC = Q$.\\\\ \n'
                        'Suy ra $MQ // AB \\Rightarrow \\dfrac{QC}{QA} = \\dfrac{MC}{MB} = %s$ suy ra $\\dfrac{AQ}{AC}=%s$. \\\\ \n'
                        %(latex(a),latex(Rational(1,a+1)) 
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='3':
                a=randint(2,9)
                h1=a/(a+1)   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Lấy điểm $M$ thuộc cạnh $BC$ sao cho $MC = %sMB$. Gọi $N, P$ lần lượt là trung điểm của $BD$ và $AD$. Gọi $Q$ là giao điểm của $AC$ với mặt phẳng $(MNP)$. Tỉ số giữa $QC$ và $AC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                                    '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8846639380149807,-2.93800878259941) rectangle (6.889799016271905,4.902902573006158); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (2.,-2.)-- (6.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,0.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (6.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (5.,4.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (2.5,2.)-- (3.5,1.); \n'
                                '\\draw [line width=1.pt] (3.5,1.)-- (3.368,-1.316); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.368,-1.316)-- (1.84,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.84,0.)-- (2.5,2.); \n'
                                '\\draw (-0.47268384983909434,0.2) node[anchor=north west] {A}; \n'
                                '\\draw (1.826430835787626,-2) node[anchor=north west] {B}; \n'
                                '\\draw (6,0.2) node[anchor=north west] {C}; \n'
                                '\\draw (5,4.5) node[anchor=north west] {D}; \n'
                                '\\draw (3.381323426645003,-1.3) node[anchor=north west] {M}; \n'
                                '\\draw (3.4,1.2) node[anchor=north west] {N}; \n'
                                '\\draw (2.1586728423810824,2.6) node[anchor=north west] {P}; \n'
                                '\\draw (1.3,0.6) node[anchor=north west] {Q}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                        'Từ giả thiết suy ra $PN // AB$. \\\\ \n'
                        'Chọn mặt phẳng phụ $(ABC)$ chứa $AC$. \\\\ \n'
                        'Hai mặt phẳng $(ABC)$ và $(MNP)$ có điểm chung $M$ và lần lượt chứa hai đường thẳng song song là $AB$, $PN$ nên giao tuyến của chúng là đường thẳng $d$ đi qua $M$ và song song với $PN$, $AB$. Trong mặt phẳng $(ABC)$, $d \\cap AC = Q$.\\\\ \n'
                        'Suy ra $MQ // AB \\Rightarrow \\dfrac{QC}{QA} = \\dfrac{MC}{MB} = %s$ suy ra $\\dfrac{QC}{AC}=%s$. \\\\ \n'
                        %(latex(a),latex(Rational(a,a+1)) 
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='2':
                a=randint(2,9)
                h1=1/a    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Lấy điểm $M$ thuộc cạnh $BC$ sao cho $MC = %sMB$. Gọi $N, P$ lần lượt là trung điểm của $BD$ và $AD$. Gọi $Q$ là giao điểm của $AC$ với mặt phẳng $(MNP)$. Tỉ số giữa $QA$ và $QC$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục). \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                                    '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8846639380149807,-2.93800878259941) rectangle (6.889799016271905,4.902902573006158); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (2.,-2.)-- (6.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,0.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (6.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (5.,4.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (2.5,2.)-- (3.5,1.); \n'
                                '\\draw [line width=1.pt] (3.5,1.)-- (3.368,-1.316); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.368,-1.316)-- (1.84,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.84,0.)-- (2.5,2.); \n'
                                '\\draw (-0.47268384983909434,0.2) node[anchor=north west] {A}; \n'
                                '\\draw (1.826430835787626,-2) node[anchor=north west] {B}; \n'
                                '\\draw (6,0.2) node[anchor=north west] {C}; \n'
                                '\\draw (5,4.5) node[anchor=north west] {D}; \n'
                                '\\draw (3.381323426645003,-1.3) node[anchor=north west] {M}; \n'
                                '\\draw (3.4,1.2) node[anchor=north west] {N}; \n'
                                '\\draw (2.1586728423810824,2.6) node[anchor=north west] {P}; \n'
                                '\\draw (1.3,0.6) node[anchor=north west] {Q}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                        'Từ giả thiết suy ra $PN // AB$. \\\\ \n'
                        'Chọn mặt phẳng phụ $(ABC)$ chứa $AC$. \\\\ \n'
                        'Hai mặt phẳng $(ABC)$ và $(MNP)$ có điểm chung $M$ và lần lượt chứa hai đường thẳng song song là $AB$, $PN$ nên giao tuyến của chúng là đường thẳng $d$ đi qua $M$ và song song với $PN$, $AB$. Trong mặt phẳng $(ABC)$, $d \\cap AC = Q$.\\\\ \n'
                        'Suy ra $MQ // AB \\Rightarrow \\dfrac{QC}{QA} = \\dfrac{MC}{MB} = %s$ suy ra $\\dfrac{QA}{QC}=%s$. \\\\ \n'
                        %(latex(a),latex(Rational(1,a)) 
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='1':
                a=randint(2,9)
                h1=a    
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Lấy điểm $M$ thuộc cạnh $BC$ sao cho $MC = %sMB$. Gọi $N, P$ lần lượt là trung điểm của $BD$ và $AD$. Gọi $Q$ là giao điểm của $AC$ với mặt phẳng $(MNP)$. Tỉ số giữa $QC$ và $QA$ bằng bao nhiêu? \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                                    '\\begin{center} \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\clip(-0.8846639380149807,-2.93800878259941) rectangle (6.889799016271905,4.902902573006158); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (2.,-2.)-- (6.,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (6.,0.)-- (0.,0.); \n'
                                '\\draw [line width=1.pt] (6.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (5.,4.)-- (2.,-2.); \n'
                                '\\draw [line width=1.pt] (0.,0.)-- (5.,4.); \n'
                                '\\draw [line width=1.pt] (2.5,2.)-- (3.5,1.); \n'
                                '\\draw [line width=1.pt] (3.5,1.)-- (3.368,-1.316); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.368,-1.316)-- (1.84,0.); \n'
                                '\\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.84,0.)-- (2.5,2.); \n'
                                '\\draw (-0.47268384983909434,0.2) node[anchor=north west] {A}; \n'
                                '\\draw (1.826430835787626,-2) node[anchor=north west] {B}; \n'
                                '\\draw (6,0.2) node[anchor=north west] {C}; \n'
                                '\\draw (5,4.5) node[anchor=north west] {D}; \n'
                                '\\draw (3.381323426645003,-1.3) node[anchor=north west] {M}; \n'
                                '\\draw (3.4,1.2) node[anchor=north west] {N}; \n'
                                '\\draw (2.1586728423810824,2.6) node[anchor=north west] {P}; \n'
                                '\\draw (1.3,0.6) node[anchor=north west] {Q}; \n'
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n'

                        'Từ giả thiết suy ra $PN // AB$. \\\\ \n'
                        'Chọn mặt phẳng phụ $(ABC)$ chứa $AC$. \\\\ \n'
                        'Hai mặt phẳng $(ABC)$ và $(MNP)$ có điểm chung $M$ và lần lượt chứa hai đường thẳng song song là $AB$, $PN$ nên giao tuyến của chúng là đường thẳng $d$ đi qua $M$ và song song với $PN$, $AB$. Trong mặt phẳng $(ABC)$, $d \\cap AC = Q$.\\\\ \n'
                        'Suy ra $MQ // AB \\Rightarrow \\dfrac{QC}{QA} = \\dfrac{MC}{MB} = %s$. \\\\ \n'
                        %(latex(a) 
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

