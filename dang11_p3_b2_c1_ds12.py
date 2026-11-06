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


def bt_dang11_p3_b2_c1_ds12(self):
            # Khai báo biến
            a=randint(1,10)
            canh = a*4
            x_2 = nsimplify(canh/2)
            dk = Rational(canh,2)
            s = round(((3)**(1/2)*(canh**2))/8,2)
            # Nội dung câu hỏi
            noidungcauhoi = ('Cho một tam giác đều $ABC$ cạnh $%s$. Người ta dựng một hình chữ nhật $MNPQ$ có cạnh $MN$ nằm trên cạnh $BC$, hai đỉnh $P$ và $Q$ theo thứ tự nằm trên cạnh $AC$ và $AB$ của tam giác. Hỏi khi hình chữ nhật $MNPQ$ có diện tích lớn nhất thì độ dài cạnh $BM$ bằng bao nhiêu?  \n'
                            %(latex(canh)))

            # Nội dung lời giải
            loigiai = ('Theo bài ta có hình vẽ \\\\ \n'
                    '\\begin{center} \n'
                        '\\begin{tikzpicture} \n'

                    '\\path  \n'
                    '(0,0) coordinate(B) \n'
                    '(4,0) coordinate (C) \n'
                    '(60:4) coordinate (A) \n'
                    '(1,0) coordinate(M) \n'
                    '(3,0) coordinate(N) \n'
                    '($(A)!0.5!(B)$) coordinate (Q) \n'
                    '($(A)!0.5!(C)$) coordinate (P) \n'
                            ';\n'

                    '\\foreach \\d/\\g in{A/90,B/-90,C/-90,Q/180,P/0,M/-90,N/-90}  \n'
                    '\\draw[fill=black](\\d)circle(0pt)node[shift={(\\g:0.35)}]{$\\d$}; \n'
                    '\\draw (A)--(C)--(B)--(A); \n'
                    '\\draw (M)--(N)--(P)--(Q)--(M); \n'
                    '\\draw (0.5,0) node[below]{$x$}; \n'
                    '\\end{tikzpicture} \n'
                    '\\end{center} \n'
                        'Đặt $BM=x$, $x \\in (0;%s)$ ta được $MN = %s-2x$, $QM=BM\\cdot \\cos60^{\\circ}=x\\sqrt{3}$. \\\\ \n'
                        'Diện tích hình chữ nhật $MNPQ$ là $S(x)=MN\\cdot QM=(%s-2x)x\\sqrt{3}=\\sqrt{3}(%sx-2x^2)$. \\\\ \n'
                        'Ta có  \\\\ \n'
                        '\\hspace*{1cm} $S\'(x)=\\sqrt{3}(%s-4x) $. \\\\ \n'
                        '\\hspace*{1cm} $S\'(x)=0 \\Leftrightarrow x = %s$. \\\\ \n'
                        '\\hspace*{1cm} Bảng biến thiên \\\\ \n'   
                        '\\begin{center}    \n'
                        '\\hspace*{1cm} \\begin{tikzpicture}    \n'
                        '\\tkzTabInit[espcl=2.5,lgt=1.5]   \n'         
                        '{$x$/1,$S\'(x)$/0.7,$S(x)$/2.1}   \n'          
                        '{$0$,$%s$,$%s$}   \n'
                        '\\tkzTabLine{,+,0,-,}   \n'
                        '\\tkzTabVar{-/$0$,+/$%s$,-/$0$}   \n'
                        '\\end{tikzpicture}   \\\\ \n'
                        '\\end{center}    \n'
                        'Từ bảng biến thiên ta thấy $S(x)$ đạt giá trị lớn nhất tại điểm $x=%s$.\\\\ \n'
                        'Vậy độ dài của cạnh $BM=%s$.'
                        %(latex(dk),latex(canh),
                        latex(canh),latex(canh),
                        latex(canh),latex(a),
                        latex(a),latex(x_2),
                        latex(s),
                        latex(a),latex(a),
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

