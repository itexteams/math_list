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


def bt_dang15_p4_b1_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                t=symbols('t')
                k=randint(1,3)
                t1=3*k
                t2=t1+6
                t3=t2+9
                dh=t**2-(t1+t2)*t+t1*t2
                f=t**3/3-(t1+t2)*t**2/2+t1*t2*t

                f0=0
                f1=Rational(t1**3,3)-Rational((t1+t2)*t1**2,2)+t1*t2*t1
                f2=Rational(t2**3,3)-Rational((t1+t2)*t2**2,2)+t1*t2*t2
                f3=Rational(t3**3,3)-Rational((t1+t2)*t3**2,2)+t1*t2*t3
                kq=f1+f1-f2+f3-f2

                # Nội dung câu hỏi
                noidungcauhoi = ('''Trên một trục số thẳng đứng có chiều dương hướng lên trên, một chất điểm bắt đầu chuyển động dọc theo trục số. Giả sử, tại thời điểm $t$ giây $(t \\ge 0))$ tính từ lúc bắt đầu chuyển động thì vị trí $s(t)$ của chất điểm trên trục số thẳng đứng được xác định bởi công thức $s(t)=%s$ mét. Trong $%s$ giây chuyển động đầu tiên, tính tổng quãng đường chất điểm đi được.'''
                                %(latex(f),latex(t3)
                                ))

                # Nội dung lời giải
                loigiai = ('''Ta có $s'(t)=%s$.\\\\
                        \\hspace*{1cm} $s'(t)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& t=%s \\\\& t=%s.}$ \\\\
                            Bảng biến thiên \\\\
            \\hspace*{1cm} \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$t$/0.7,$s'$/0.7,$s$/2.1}
            {$0$,$%s$,$%s$,$%s$}
            \\tkzTabLine{,+,0,-,0,+,}
            \\tkzTabVar{-/$%s$,+/$%s$,-/$%s$,+/$%s$}
            \\end{tikzpicture} \\\\
            Trong $%s$ giây đầu tiên, chất điểm di chuyển hướng lên $%s$ mét. \\\\
            Trong khoảng (%s;%s) giây tiếp theo, chất điểm di chuyển hướng xuống $%s$ mét. \\\\      
            Trong khoảng (%s;%s) giây cuối, chất điểm di chuyển hướng lên $%s$ mét. \\\\ 
                Vậy trong $%s$ giây đầu tiên chất điểm chuyển động được quãng đường là $%s+%s+%s=%s$ mét.'''
                        %(latex(dh),latex(dh),latex(t1),latex(t2),
                            latex(t1),latex(t2),latex(t3),
                            latex(f0),latex(f1),latex(f2),latex(f3),
                            latex(t1),latex(f1),
                            latex(t1),latex(t2),latex(f1-f2),
                            latex(t2),latex(t3),latex(f3-f2),
                            latex(t3),latex(f1),latex(f1-f2),latex(f3-f2),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content  

