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


def bt_dang2_p4_b3_c1_hh12(self):
            # Khai báo biến
            a1=randint(10,25)
            b1=randint(15,35)
            c1=randint(10,20)
            d1=randint(15,40)
            a=a1/10
            b=b1/10
            c=c1/10
            d=d1/10
            e=sqrt(b**2+c**2+(d-a)**2)
            number = Decimal(float(e))  # Số cần làm tròn
            kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
            # Nội dung câu hỏi
            noidungcauhoi = ('Hình bên dưới mô tả hai bức tường gạch được xây vuông góc với nhau và cùng vuông góc với mặt đất$zz$ Một người thợ xây căng dây giữa hai bức tường$zz$ Đầu A của sợi dây trên bức tường thứ nhất, cách bức tường thứ hai là %s m và cách mặt đất là %s m$zz$ Đầu B của sợi dây nằm trên bức tường thứ hai, cách bức tường thứ nhất là %s m và cách mặt đất là %s m$zz$ Tính độ dài của sợi dây được căng bởi hai đầu $AB$ (làm tròn kết quả đến hàng phần trăm)$zz$  \n'
                            '\\begin{center}\n'
                        '\\begin{tikzpicture} \n'
                            '\\path \n'
                            '(0,0) coordinate (O)\n'
                            '(0,5) coordinate (A) \n'
                            '(6,0) coordinate (B)\n'
                            '(-135:5) coordinate (C) \n'
                            '(-2,-2) coordinate (D) \n'
                            '(-2,0) coordinate (E) \n'
                            '(3,3) coordinate (F)\n'
                            '(3,0) coordinate (G);\n'
                            '\\fill[cyan!20] (O)--(5,0)--(5,4)--(0,4);--cycle; \n'
                            '\\fill[orange!20] (O)--(5,0)--(2,-3)--(-135:4$zz$24);--cycle; \n'
                            '\\fill[magenta!20] (O)--(-135:4$zz$24)--(-3,1)--(0,4);--cycle; \n'
                            '\\path \n' 
                            '($(F)!1/2!(G)$) node[right]{%s m} \n' 
                            '($(F)!1/2!(0,3)$) node[above]{%s m} \n'
                            '($(D)!2/3!(E)$) node[right]{%s m}\n'
                            '(-2,0) node[above left]{$A$} \n'
                            '(3,3) node[above right]{$B$}\n'
                            '($(0,2)!1/2!(E)$) node[above left]{%s m};  \n'
                            '\\draw[dashed](F)--(G); \n'
                            '\\draw[dashed](F)--(0,3);\n'
                            '\\draw[dashed](E)--(0,2);\n'
                            '\\draw[dashed](E)--(D); \n'
                            '\\draw (E)--(F); \n'
                            '\\draw(5,0)--(5,4)--(0,4);\n' 
                            '\\draw(5,0)--(2,-3)--(-135:4$zz$24);\n' 
                            '\\draw(-135:4$zz$24)--(-3,1)--(0,4);\n'
                            '\\draw (O)--(0,4);\n' 
                            '\\draw (O)--(5,0); \n'
                            '\\draw (O)--(-135:4$zz$24); \n'
                            '\\foreach \\d/\\g in{D/90,F/90,G/180,E/90}  \n'
                            '\\draw[fill=black](\\d)circle(1$zz$5pt);  \n'
                        '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                            %(latex(b),latex(a),latex(c),latex(d),latex(d),latex(c),latex(a),latex(b))
                            )
            # Nội dung lời giải
            loigiai = ('\\begin{center}  \n'
                            '\\begin{tikzpicture}  \n'
                                '\\path  \n'
                                '(0,0) coordinate (O) \n'
                                '(0,5) coordinate (A) \n' 
                                '(6,0) coordinate (B) \n'
                                '(-135:5) coordinate (C)  \n'
                                '(-2,-2) coordinate (D)  \n'
                                '(-2,0) coordinate (E)  \n'
                                '(3,3) coordinate (F) \n'
                                '(3,0) coordinate (G); \n'
                                '\\fill[cyan!20] (O)--(5,0)--(5,4)--(0,4);--cycle;  \n'
                                '\\fill[orange!20] (O)--(5,0)--(2,-3)--(-135:4$zz$24);--cycle;  \n'
                                '\\fill[magenta!20] (O)--(-135:4$zz$24)--(-3,1)--(0,4);--cycle;  \n'
                                '\\path   \n'
                                '($(F)!1/2!(G)$) node[right]{%s m}   \n'
                                '($(F)!1/2!(0,3)$) node[above]{%s m}  \n'
                                '($(D)!2/3!(E)$) node[right]{%s m} \n'
                                '(-2,0) node[above left]{$A$}  \n'
                                '(3,3) node[above right]{$B$} \n'
                                '($(0,2)!1/2!(E)$) node[above left]{%s m};  \n' 
                                '\\draw[dashed](F)--(G);  \n'
                                '\\draw[dashed](F)--(0,3); \n'
                                '\\draw[dashed](E)--(0,2); \n'
                                '\\draw[dashed](E)--(D);  \n'
                                '\\draw (E)--(F);  \n'
                                '\\draw(5,0)--(5,4)--(0,4);  \n'
                                '\\draw(5,0)--(2,-3)--(-135:4$zz$24); \n' 
                                '\\draw(-135:4$zz$24)--(-3,1)--(0,4);  \n'
                                '\\draw[->] (O)--(A) node[left] {$z$};  \n'
                                '\\draw[->] (O)--(B) node[above] {$y$};  \n'
                                '\\draw[->] (O)--(C) node[above] {$x$}; \n'
                                '\\draw (O) node[below right]{$O$}; \n'
                                '\\foreach \\d/\\g in{O/45,D/90,F/90,G/180,E/90}   \n'
                                '\\draw[fill=black](\\d)circle(1$zz$5pt);  \n' 
                            '\\end{tikzpicture}  \n'
                        '\\end{center}  \n' 
                        '\\hspace*{1cm}Chọn hệ trục tọa độ $Oxyz$ có gốc $O$ trùng với góc phòng, các trục $Ox, Oy, Oz$ trùng với các mép tường như hình vẽ$zz$ Đơn vị trong không gian $Oxyz$ được lấy theo mét$zz$ Khi đó tọa độ của hai đầu dây A, B là $A(%s;0;%s)$ và $B(0;%s;%s)$$zz$\\\\  \n'
                        '\\hspace*{1cm}Vậy độ dài của sợi dây là  \n' 
                        '$AB=\\sqrt{(0-%s)^2+(%s-0)^2+(%s-%s)^2} \\approx %s$ (m)$zz$  \n'

                        %(latex(d),latex(c),latex(a),latex(b),
                        latex(b),latex(a),latex(c),
                        latex(d),latex(b),latex(c),
                        latex(d),latex(a),latex(kq),

                        )
                        )
            #Đáp án


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content                                                        

