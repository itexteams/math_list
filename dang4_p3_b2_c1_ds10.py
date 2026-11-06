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


def bt_dang4_p3_b2_c1_ds10(self):
            # Khai báo biến
            lista=['Nam','Bình','Sơn','Tài','Tiến','Cường','Lâm','Trọng','Chiến','Dũng','Hưng','Quang','Lập','Phi','Hòa','Hải','Chung','Đạo','Hồng']
            t1=random.choice(lista)
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a = randint(10,25)
                b = randint(10,25)
                c = randint(5,12)
                while c>=a or c>=b or a+b-c>=30:
                    a = randint(10,25)
                    b = randint(10,25)
                    c = randint(5,12)
                # Nội dung câu hỏi
                noidungcauhoi = ('Bạn %s thống kê số ngày có mưa, có sương mù tại nơi mình ở trong tháng 3 vào một thời điểm nhất định và được kết quả như sau: '
                                '%s ngày có mưa, %s ngày có sương mù, trong đó %s ngày có cả mưa và sương mù$zz$ '
                                'Hỏi trong tháng 3 đó có bao nhiêu ngày không có mưa và không có sương mù? \n'
                                %(str(t1),latex(a),latex(b),latex(c))
                                )

                # Nội dung lời giải
                loigiai = ('Gọi $A,B$ lần lượt là tập hợp các ngày có mưa, có sương mù$zz$ Khi đó, $A\\cap B$ là tập hợp các ngày có cả mưa và sương mù, $A\\cup B$ là tập hợp các ngày hoặc có mưa hoặc có sương mù$zz$ \\\\'
                        'Ta có: $n(A)=%s,n(B)=%s,n(A\\cap B)=%s$$zz$ \\\\ '
                        'Số ngày hoặc có mưa hoặc có sương mù là: \\\\'
                        '\\hspace*{3cm}$n(A\\cup B)=n(A)+n(B)-n(A\\cap B)=%s+%s-%s=%s$ (ngày)$zz$ \\\\ '
                        'Tháng 3 có 31 ngày nên số ngày không có mưa và không có sương mù trong tháng 3 đó là:\\\\ '
                        '$31-%s=%s$ ngày$zz$'
                        %(latex(a),latex(b),latex(c),
                            latex(a),latex(b),latex(c),latex(a+b-c),
                            latex(a+b-c),latex(31-a-b+c))
                            )
                hinhve = (	'\\hspace*{6cm}\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick,scale=1$zz$5]\\\\ \n'
                            '\\draw[black] (0,0) circle (1cm);\\\\ '
                            '\\node at (-0$zz$5,0$zz$2) {$%s$};\\\\ '
                            '\\draw[black] (1,0) circle (1cm);\\\\ '
                            '\\node at (1$zz$5,0$zz$2) {$%s$};\\\\ '
                            '\\node at (0$zz$5,0) {$%s$};\\\\ '
                                '\\begin{scope}\\\\ '
                                '\\clip (0,0) circle (1cm);\\\\ '
                                '\\clip (1,0) circle (1cm);\\\\ '
                                '\\fill[pattern=north east lines, pattern color=black] (1,0) circle (1cm);\\\\ '
                                '\\end{scope}\\\\ '
                        '\\end{tikzpicture}\\\\ ' %(latex(a),latex(b),latex(c)))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(31-a-b+c))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(hinhve)+'\n'''+str(loigiai)+'}'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content  

