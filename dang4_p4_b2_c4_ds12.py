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


def bt_dang4_p4_b2_c4_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,5)
                pa=a/10
                p_a=1-pa
                b=randint(5,9)
                pb=b/10
                p_b=1-pb
                kq=pa*p_b+p_a*pa

                # Câu hỏi
                noidungcauhoi = ('Ông Nam hằng ngày đi làm bằng xe máy hoặc xe buýtzz Nếu hôm nay ông đi làm bằng xe buýt thì xác suất để hôm sau ông đi làm bằng xe máy là $%s$zz Nếu hôm nay ông đi làm bằng xe máy thì xác suất để hôm sau ông đi làm bằng xe buýt là $%s$zz Xét một tuần mà thứ Hai ông Nam đi làm bằng xe buýtzz Tính xác suất để thứ Tư trong tuần đó, ông Nam đi làm bằng xe máyzz'
                                %(latex(pa),latex(pb)
                                ))

                # Nội dung lời giải
                loigiai=('Gọi các biến cố: \\\\ \n'
                        '\\hspace*{1cm} $A$:"Thứ Ba, ông Nam đi làm bằng xe máy"zz \\\\ \n'
                        '\\hspace*{1cm} $B$:"Thứ Tư, ông Nam đi làm bằng xe máy"zz \\\\ \n'
                        'Ta cần tính $P(B)$zz Theo công thức xác suất toàn phần, ta có \n'
                        '$$P(B)=P(A) \\cdot P(B | A) +P(\\overline{A}) \\cdot P(B | \\overline{A})zz$$'
                        'Tính $P(A)$: \\\\ \n'
                        '\\hspace*{1cm} Vì thứ Hai, ông Nam đi làm bằng xe buýt nên xác suất để thứ Ba (hôm sau), ông đi làm bằng xe máy là $%s$, nên $P(A)=%s$zz \\\\ \n'
                        'Tính $P(\\overline{A})$: \\\\ \n'
                        '\\hspace*{1cm} Ta có $P(\\overline{A})=1-%s=%s$zz \\\\ \n'
                        'Tính $P(B|A)$: \\\\ \n'
                        '\\hspace*{1cm} Đây là xác suất để thứ Tư, ông Nam đi làm bằng xe máy nếu thứ Ba, ông Nam đi làm bằng xe máyzz Theo giả thiết, nếu hôm nay ông đi làm bằng xe máy thì xác suất để hôm sau ông đi làm bằng xe buýt là $%s$ và đi làm bằng xe máy là $1-%s=%s$zz Do đó, nếu thứ Ba, ông Nam đi làm bằng xe máy thì xác suất để thứ Tư, ông đi làm bằng xe máy là $%s$zz Vậy $P(B|A)=%s$zz  \\\\ \n'
                        'Tính $P(B| \\overline{A})$: \\\\ \n'
                        '\\hspace*{1cm} Đây là xác suất để thứ Tư, ông Nam đi làm bằng xe máy nếu thứ Ba ông Nam đi làm bằng xe buýt. Theo giả thiết, nếu hôm nay ông đi làm bằng xe buýt thì xác suất để hôm sau ông đi làm bằng xe máy là $%s$zz Do đó, nếu thứ Ba, ông đi làm bằng xe buýt thì xác suất để thứ Tư, ông đi làm bằng xe máy là $%s$zz Suy ra $P(B| \\overline{A})=%s$zz \\\\ \n'
                        'Vậy \n'
                        '$$P(B)=P(A) \\cdot P(B | A) +P(\\overline{A}) \\cdot P(B | \\overline{A})=%s \\cdot %s+%s \\cdot %s =%szz$$'
                        %(latex(pa),latex(pa),
                        latex(pa),latex(p_a),
                        latex(pb),latex(pb),latex(p_b),latex(p_b),latex(p_b),
                        latex(pa),latex(pa),latex(pa),
                        latex(pa),latex(p_b),latex(p_a),latex(pa),latex(kq)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content 

