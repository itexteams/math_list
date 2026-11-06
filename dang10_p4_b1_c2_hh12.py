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


def bt_dang10_p4_b1_c2_hh12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)

            if dang=='1':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(a,h)
                a1=nsimplify(u/-a)
                b1=nsimplify(u/-a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*a+b1*0+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)

                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                    'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $C$ đến mặt phẳng $(SAB)$.'
                                '}{'
                        '\\scalebox{0.6}{ '          
                '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'

                    %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SAB)$ đi qua các điểm $S(0;0;%sa),A(-%sa;0;0),B(0;-%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{-%sa}+\\dfrac{y}{-%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $C$ đến mặt phẳng $(SAB)$ là\\\\ \n'
                        '$$d(C,(SAB))=\\dfrac{\\abs{%s\\cdot %sa+%s\\cdot 0+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(a),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='2':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(a,h)
                a1=nsimplify(u/-a)
                b1=nsimplify(u/-a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*0+b1*a+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $D$ đến mặt phẳng $(SAB)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'

                    %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SAB)$ đi qua các điểm $S(0;0;%sa),A(-%sa;0;0),B(0;-%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{-%sa}+\\dfrac{y}{-%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $D$ đến mặt phẳng $(SAB)$ là\\\\ \n'
                        '$$d(D,(SAB))=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot %sa+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(b1),latex(a),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='3':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(-a,h)
                a1=nsimplify(u/-a)
                b1=nsimplify(u/a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*0+b1*(-a)+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $B$ đến mặt phẳng $(SAD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'

                    %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SAD)$ đi qua các điểm $S(0;0;%sa),A(-%sa;0;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{-%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $B$ đến mặt phẳng $(SAD)$ là\\\\ \n'
                        '$$d(B,(SAD))=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot (-%sa)+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(b1),latex(a),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='4':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(-a,h)
                a1=nsimplify(u/-a)
                b1=nsimplify(u/a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*a+b1*0+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $C$ đến mặt phẳng $(SAD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'

                    %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SAD)$ đi qua các điểm $S(0;0;%sa),A(-%sa;0;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{-%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $C$ đến mặt phẳng $(SAD)$ là\\\\ \n'
                        '$$d(C,(SAD))=\\dfrac{\\abs{%s\\cdot %sa+%s\\cdot 0+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(a),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='5':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(a,h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*(-a)+b1*0+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SCD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'
                %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$\\\\ \n'
                        'Vì mặt phẳng $(SCD)$ đi qua các điểm $S(0;0;%sa),C(%sa;0;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $A$ đến mặt phẳng $(SCD)$ là\\\\ \n'
                        '$$d(A,(SCD))=\\dfrac{\\abs{%s\\cdot (-%sa)+%s\\cdot 0+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(a),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='6':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(a,h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*0+b1*(-a)+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $B$ đến mặt phẳng $(SCD)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'

                %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SCD)$ đi qua các điểm $S(0;0;%sa),C(%sa;0;0),D(0;%sa;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $B$ đến mặt phẳng $(SCD)$ là\\\\ \n'
                        '$$d(B,(SCD))=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot (-%sa)+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(b1),latex(a),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='7':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(-a,h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/-a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*(-a)+b1*0+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)





                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$.'
                                '}{'
                    '\\scalebox{0.6}{ '  
                    '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'
                %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SBC)$ đi qua các điểm $S(0;0;%sa),B(0;-%sa;0),C(%sa;0;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{-%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $A$ đến mặt phẳng $(SBC)$ là\\\\ \n'
                        '$$d(A,(SBC))=\\dfrac{\\abs{%s\\cdot (-%sa)+%s\\cdot 0+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(a),latex(b1),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            if dang=='8':
                # Khai báo biến
                x,y,z=symbols('x,y,z')
                a=randint(2,12)
                h=randint(2,12)
                u=lcm(-a,h)
                a1=nsimplify(u/a)
                b1=nsimplify(u/-a)
                c1=nsimplify(u/h)
                d1=-u
                pt=a1*x+b1*y+c1*z+d1
                tu=abs(a1*0+b1*a+c1*0+d1)
                mau=sqrt(a1**2+b1**2+c1**2)
                kq=nsimplify(tu/mau)

                # Nội dung câu hỏi
                noidungcauhoi =  ('\\immini{'
                                'Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $%sa\\sqrt{2}$, chiều cao bằng $%sa$ và $O$ là tâm của đáy. Bằng cách thiết lập tọa độ như hình vẽ. Tính khoảng cách từ điểm $D$ đến mặt phẳng $(SBC)$.'
                                '}{'
                        '\\scalebox{0.6}{ '  
                        '\\begin{tikzpicture}[scale=0.8,>=stealth, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\clip(-5,-2.5) rectangle (8,6);\n'
                '\\draw[dashed] (-2,1)-- (-4,-1);\n'
                '\\draw(-4,-1)-- (1,-1);\n'
                '\\draw (1,-1)-- (3,1);\n'
                '\\draw [dashed] (3,1)-- (-2,1);\n'
                '\\draw [dashed]  (-2,1)-- (1,-1);\n'
                '\\draw [dashed] (-4,-1)-- (3,1);\n'
                '\\draw [dashed](-0.5,0)-- (-0.44,4.3);\n'
                '\\draw [dashed] (-0.44,4.3)-- (-2,1);\n'
                '\\draw (-0.44,4.3)-- (-4,-1);\n'
                '\\draw  (-0.44,4.3)-- (3,1);\n'
                '\\draw (-0.44,4.3)-- (1,-1);\n'
                '\\draw [->] (3,1) -- (4.338284734133795,1.38236706689537);\n'
                '\\draw [->] (1,-1) -- (2.303636363636366,-1.8690909090909107);\n'
                '\\draw [->] (-0.44,4.3) -- (-0.42573976886215636,5.3219832315454605);\n'
                '\\draw (-0.2680693819321126,5) node[right] {$z$};\n'
                '\\draw (2.1693343940990037,-2.4) node[above] {$y$};\n'
                '\\draw (3.9,1.3) node[above] {$x$};\n'
                '\\begin{scriptsize}\n'
                    '\\draw (-2.014011093840926,0.7) node {$A$};\n'
                    '\\draw (-4,-1.4) node {$B$};\n'
                    '\\draw (0.85,-1.3) node {$C$};\n'
                    '\\draw (3.0855216290610548,0.6) node {$D$};\n'
                    '\\draw (-0.6310869655963215,-0.15958591833577762) node[below] {$O$};\n'
                    '\\draw (-0.75,4.6) node[below] {$S$};\n'
                '\\end{scriptsize}\n'
                '\\end{tikzpicture} }}\n'
                    %(latex(a), latex(h)))

                # Nội dung lời giải
                loigiai = ('Ta có $AC=BD=%sa\\sqrt{2}\\cdot\\sqrt{2}=%sa$.\\\\ \n'
                        'Suy ra $OA=OB=OC=OD=\\dfrac{%sa}{2}=%sa$.\\\\ \n'
                        'Chọn gốc tọa độ là $O(0;0;0)$ ta có\\\\ \n'
                        '$A(-%sa;0;0),B(0;-%sa;0),C(%sa;0;0),D(0;%sa;0),S(0;0;%sa)$.\\\\ \n'
                        'Vì mặt phẳng $(SBC)$ đi qua các điểm $S(0;0;%sa),B(0;-%sa;0),C(%sa;0;0)$ nên có phương trình là\\\\ \n'
                        '$$\\dfrac{x}{%sa}+\\dfrac{y}{-%sa}+\\dfrac{z}{%sa}=1\\Leftrightarrow %s+%sa=0.$$\\\\ \n'
                        'Khoảng cách từ điểm $D$ đến mặt phẳng $(SBC)$ là\\\\ \n'
                        '$$d(D,(SBC))=\\dfrac{\\abs{%s\\cdot 0+%s\\cdot %sa+%s\\cdot 0+%sa}}{\\sqrt{(%s)^2+(%s)^2+(%s)^2}}=%sa.$$'

                        %(latex(a),latex(2*a),latex(2*a),latex(a),
                            latex(a),latex(a),latex(a),latex(a),latex(h),
                            latex(h),latex(a),latex(a),
                            latex(a),latex(a),latex(h),latex(pt-d1),latex(d1),
                            latex(a1),latex(b1),latex(a),latex(c1),latex(d1),latex(a1),latex(b1),latex(c1),
                            latex(kq),

                            )
                        )
            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('+-','-').replace('-1\\cdot','-').replace('+1\\cdot','+').replace('{1\\cdot','{')
            return content 

