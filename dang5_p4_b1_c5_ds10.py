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


def bt_dang5_p4_b1_c5_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a1=['0,1,2,3,4','0,1,2,3,4,5','0,1,2,3,4,5,6','0,1,2,3,4,5,6,7','0,1,2,3,4,5,6,7,8']
                a=random.choice(a1)
                b1=[2,3,4,5]
                b=random.choice(b1)
                # Câu hỏi
                noidungcauhoi='''Từ các chữ số $%s$ có thể lập được bao nhiêu số tự nhiên gồm $%s$ chữ số đôi một khác nhau?''' %(str(a), latex(b))

                # Nội dung lời giải
                if b==2 and a=='0,1,2,3,4':
                    loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $4 \\cdot 4 = 16$ số tự nhiên cần lập.'
                        )
                if b==2 and a=='0,1,2,3,4,5':
                    loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $5 \\cdot 5 = 25$ số tự nhiên cần lập.'
                        )
                if b==2 and a=='0,1,2,3,4,5,6':
                    loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $6 \\cdot 6 = 36$ số tự nhiên cần lập.'
                        )
                if b==2 and a=='0,1,2,3,4,5,6,7':
                    loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $7 \\cdot 7 = 49$ số tự nhiên cần lập.'
                        )
                if b==2 and a=='0,1,2,3,4,5,6,7,8':
                    loigiai=( 'Gọi số cần lập là $\\overline{ab}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $8 \\cdot 8 = 64$ số tự nhiên cần lập.'
                        )

                if b==3 and a=='0,1,2,3,4':
                    loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 = 48$ số tự nhiên cần lập.'
                        )
                if b==3 and a=='0,1,2,3,4,5':
                    loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 = 100$ số tự nhiên cần lập.'
                        )
                if b==3 and a=='0,1,2,3,4,5,6':
                    loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 = 180$ số tự nhiên cần lập.'
                        )
                if b==3 and a=='0,1,2,3,4,5,6,7':
                    loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 = 294$ số tự nhiên cần lập.'
                        )
                if b==3 and a=='0,1,2,3,4,5,6,7,8':
                    loigiai=( 'Gọi số cần lập là $\\overline{abc}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 = 448$ số tự nhiên cần lập.'
                        )
                if b==4 and a=='0,1,2,3,4':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 \\cdot 2 = 96$ số tự nhiên cần lập.'
                        )
                if b==4 and a=='0,1,2,3,4,5':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 \\cdot 3 = 300$ số tự nhiên cần lập.'
                        )
                if b==4 and a=='0,1,2,3,4,5,6':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 \\cdot 4 = 720$ số tự nhiên cần lập.'
                        )
                if b==4 and a=='0,1,2,3,4,5,6,7':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 \\cdot 5 = 1470$ số tự nhiên cần lập.'
                        )
                if b==4 and a=='0,1,2,3,4,5,6,7,8':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcd}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 \\cdot 6 = 2688$ số tự nhiên cần lập.'
                        )
                if b==5 and a=='0,1,2,3,4':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 4 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 1 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $4 \\cdot 4 \\cdot 3 \\cdot 2 \\cdot 1 = 96$ số tự nhiên cần lập.'
                        )
                if b==5 and a=='0,1,2,3,4,5':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 5 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 2 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $5 \\cdot 5 \\cdot 4 \\cdot 3 \\cdot 2 = 600$ số tự nhiên cần lập.'
                        )
                if b==5 and a=='0,1,2,3,4,5,6':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 6 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 3 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $6 \\cdot 6 \\cdot 5 \\cdot 4 \\cdot 3 = 2160$ số tự nhiên cần lập.'
                        )
                if b==5 and a=='0,1,2,3,4,5,6,7':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 7 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 4 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $7 \\cdot 7 \\cdot 6 \\cdot 5 \\cdot 4 = 5880$ số tự nhiên cần lập.'
                        )
                if b==5 and a=='0,1,2,3,4,5,6,7,8':
                    loigiai=( 'Gọi số cần lập là $\\overline{abcde}$, với $a, b$ là ba chữ số đôi một khác nhau từ các chữ số đã cho.\\\\'
                        'Có 8 cách chọn chữ số $a$ từ các chữ số đã cho. \\\\'
                        'Ứng với mỗi cách chọn đó, có 8 cách chọn chữ số $b$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 7 cách chọn chữ số $c$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 6 cách chọn chữ số $d$ từ các chữ số còn lại. \\\\'
                        'Ứng với mỗi cách chọn đó, có 5 cách chọn chữ số $e$ từ các chữ số còn lại. \\\\'
                        'Áp dụng quy tắc nhân ta có $8 \\cdot 8 \\cdot 7 \\cdot 6 \\cdot 5 = 13440$ số tự nhiên cần lập.'
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-')
            return content        


