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


def bt_dang2_p4_b2_c1_hh10(self):
            # Khai báo biến
            lis1=[2,3,4,5,6,7]
            a=random.choice(lis1)
            b=randint(10,20)

            lis2=[50,55,60,65,70,75]
            goc1=random.choice(lis2)
            goc1_rad=goc1 * pi / 180

            lis3=[45,40,35,30]
            goc2=random.choice(lis3)
            goc2_rad=goc2 * pi / 180

            goc3=goc1-goc2
            goc3_rad=goc3 * pi / 180

            goc4=90-goc1
            goc4_rad=goc4 * pi / 180

            kq1=round(a*sin(goc4_rad)/sin(goc3_rad),1)
            kq2=round(kq1*sin(goc2_rad),1)
            kq9=kq2+b
            number = Decimal(float(kq9))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            lisi=[1,2,3,-1,-2,-3]
            i1=random.choice(lisi)
            lisi.remove(i1)
            i2=random.choice(lisi)
            lisi.remove(i2)
            i3=random.choice(lisi)
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                            'Trên nóc tòa nhà có một cột ăng-ten cao $%s$ m$zzz$ Từ một vị trí quan sát $A$ cao $%s$ m so với mặt đất có thể nhìn thấy đỉnh $B$ và chân $C$ của cột ăng-ten với các góc tương ứng $%s^\\circ$ và $%s^\\circ$ so với phương nằm ngang$zzz$ Tính chiều cao của tòa nhà$zzz$ (làm tròn kết quả đến hàng phần mười)$zzz$  \n'
                            '}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0$zzz$8]  \n'
                        '\\draw (0,5) node[above left]{$C$};  \n'
                        '\\draw (0,7) node[above left]{$B$};  \n'
                        '\\draw (4,2) node[below left]{$A$};  \n'
                        '\\draw (0,2) node[below right]{$D$}; \n'
                        '\\draw (4,1) node[below left]{$%s$m};  \n'
                        '\\draw (0,6) node[above left]{$%s$m};  \n'
                        '\\coordinate (O) at (0,0);   \n'
                        '\\coordinate (M1) at (-1,0);    \n'
                        '\\coordinate (M2) at (-2,0);   \n'
                        '\\coordinate (M3) at (4,0);   \n'
                        '\\coordinate (M4) at (5,0);   \n'
                        '\\coordinate (M5) at (0,2); \n'
                        '\\coordinate (C) at (0,5);  \n'
                        '\\coordinate (B) at (0,7);  \n'
                        '\\coordinate (M6) at (-1,5);  \n'
                        '\\coordinate (A) at (4,2);  \n'
                        '\\coordinate (M7) at (5,2);  \n'
                        '\\draw[name path=OM1] (O)--(M4);    \n'
                        '\\draw[name path=OM2] (O)--(M2);  \n'
                        '\\draw[name path=OM2] (O)--(B);  \n'
                        '\\draw[name path=OM2] (M1)--(M6);  \n'
                        '\\draw[name path=OM2] (C)--(M6);  \n'
                        '\\draw[name path=OM2] (A)--(M3);  \n'
                        '\\draw[dashed] (M5)--(M7);  \n'
                        '\\draw[dashed] (A)--(C);  \n'
                        '\\draw[dashed] (A)--(B);  \n'
                        '\\fill[pattern=north east lines, pattern color=black, opacity=1] (0,0) -- (0,5) -- (-1,5) -- (-1,0) -- cycle;  \n'
                        '\\fill[pattern=north east lines, pattern color=black, opacity=1] (-2,0) -- (5,0) -- (5,-0$zzz$2) -- (-2,-0$zzz$2) -- cycle;  \n'
                    '\\end{tikzpicture} \\\\ \n'
                            '} \n'
                            %(latex(a),latex(b),latex(goc1),latex(goc2),
                            latex(b), latex(a)
                            ))
                # Hình vẽ
                hinhve=('\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick, scale=0$zzz$8]  \n'
                        '\\draw (0,5) node[above left]{$C$};  \n'
                        '\\draw (0,7) node[above left]{$B$};  \n'
                        '\\draw (4,2) node[below left]{$A$};  \n'
                        '\\draw (0,2) node[below right]{$D$}; \n'
                        '\\draw (4,1) node[below left]{$%s$m};  \n'
                        '\\draw (0,6) node[above left]{$%s$m};  \n'
                        '\\coordinate (O) at (0,0);   \n'
                        '\\coordinate (M1) at (-1,0);    \n'
                        '\\coordinate (M2) at (-2,0);   \n'
                        '\\coordinate (M3) at (4,0);   \n'
                        '\\coordinate (M4) at (5,0);   \n'
                        '\\coordinate (M5) at (0,2); \n'
                        '\\coordinate (C) at (0,5);  \n'
                        '\\coordinate (B) at (0,7);  \n'
                        '\\coordinate (M6) at (-1,5);  \n'
                        '\\coordinate (A) at (4,2);  \n'
                        '\\coordinate (M7) at (5,2);  \n'
                        '\\draw[name path=OM1] (O)--(M4);    \n'
                        '\\draw[name path=OM2] (O)--(M2);  \n'
                        '\\draw[name path=OM2] (O)--(B);  \n'
                        '\\draw[name path=OM2] (M1)--(M6);  \n'
                        '\\draw[name path=OM2] (C)--(M6);  \n'
                        '\\draw[name path=OM2] (A)--(M3);  \n'
                        '\\draw[dashed] (M5)--(M7);  \n'
                        '\\draw[dashed] (A)--(C);  \n'
                        '\\draw[dashed] (A)--(B);  \n'
                        '\\fill[pattern=north east lines, pattern color=black, opacity=1] (0,0) -- (0,5) -- (-1,5) -- (-1,0) -- cycle;  \n'
                        '\\fill[pattern=north east lines, pattern color=black, opacity=1] (-2,0) -- (5,0) -- (5,-0$zzz$2) -- (-2,-0$zzz$2) -- cycle;  \n'
                    '\\end{tikzpicture} \\\\ \n'
                    %(latex(b), latex(a)
                        ) )
                # Nội dung lời giải
                loigiai = ('Theo bài toán ta có \\\\ \n'
                        '$\\widehat{BAD}=%s^\\circ$ và $\\widehat{CAD}=%s^\\circ$ nên $\\widehat{BAC}=%s^\\circ-%s^\\circ=%s^\\circ$$zzz$ \\\\ \n'
                        '$\\widehat{ABC}=90^\\circ-\\widehat{BAD}=90^\\circ-%s^\\circ=%s^\\circ$$zzz$ \\\\ \n'
                        'Áp dụng định lí sin trong tam giác $ABC$ ta có \\\\ \n'
                        '$\\dfrac{BC}{\\sin A}=\\dfrac{AC}{\\sin B} \\Rightarrow AC=\\dfrac{BC \\cdot \\sin B}{\\sin A} =\\dfrac{%s \\cdot \\sin %s^\\circ}{\\sin %s^\\circ} \\approx %s $$zzz$\\\\ \n'
                        'Xét tam giác $ACD$ vuông tại $D$, ta có $CD=AC \\cdot \\sin %s^\\circ \\approx %s$$zzz$ \\\\ \n'
                        'Vậy chiều cao của tòa nhà là $%s+%s \\approx %s$ m$zzz$'
                        %(latex(goc1), latex(goc2),latex(goc1), latex(goc2),latex(goc3),
                        latex(goc1), latex(goc4),latex(a), latex(goc4), latex(goc3),latex(kq1),
                        latex(goc2),latex(kq2),
                        latex(kq2),latex(b),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +hinhve
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n').replace('.',',').replace('$zzz$','.').replace('{,}0','').replace('\\frac','\\dfrac').replace('+-','-')

            return content   

