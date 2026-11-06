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


def bt_dang6_p1_b1_c2_ds10(self):
            #Khai báo biến
            x = symbols('x')
            y = symbols('y')
            lis_a=[300,350,400,450,500,550,600,650,700,750,800,850,900]
            a=random.choice(lis_a) #Phí cố định thứ 2 đến thứ 6
            lis_b=[1000,1100,1200,1300,1400,1500]
            b=random.choice(lis_b) #Phí cố định T7, CN
            c=randint(5,10)
            d=randint(10,20)
            e=randint(10,20)
            bt1=c*x+5*a+d*y+2*b
            bpt=c*x+5*a+d*y<=e*1000-2*b
            kq=simplify(bpt) #rút gọn hệ số
            bpt1=c*x+5*a+d*y>=e*1000-2*b
            kq1=simplify(bpt1) #rút gọn hệ số
            bpt2=c*x+5*a+d*y<e*1000+2*b
            kq2=simplify(bpt2) #rút gọn hệ số
            bpt3=c*x+5*a+d*y>e*1000+2*b
            kq3=simplify(bpt3) #rút gọn hệ số

            #Nội dung câu hỏi
            noidungcauhoi = ('Một người muốn thuê một chiếc ô tô (có lái xe) trong một tuần. Giá thuê xe được cho như bảng sau: \\\\ \n'
                            '\\begin{center} \n'
                            '\\begin{tabular}{|c|c|c|} \n'
                                '\\hline  \n'
                                '&Phí cố định  &Phí tính theo quãng đường di chuyển \\\\ \n'
                                '&(nghìn đồng/ngày)  &(nghìn đồng/kilômét)  \\\\ \n'
                                '\\hline \n'
                                'Từ thứ Hai đến thứ Sáu& $%s$  & $%s$  \\\\ \n'
                                '\\hline \n'
                                'Thứ Bảy và Chủ nhật& $%s$  & $%s$  \\\\ \n'
                                '\\hline \n'
                            '\\end{tabular} \n'
                            '\\end{center} \n'
                            'Gọi $x$ và $y$ lần lượt là số kilômét người này đi trong các ngày từ thứ Hai đến thứ Sáu và trong hai ngày cuối tuần. Bất phương trình biểu thị mỗi liên hệ giữa $x$ và $y$ sao cho tổng số tiền người đó phải trả không quá $%s$ triệu đồng là'
                            %(latex(a),latex(c),latex(b),latex(d),latex(e)
                            ) )
            # Các đáp án
            da_d = '\\True $%s$'%(latex(kq))
            da_s1 = '$%s$'%(latex(kq1))
            da_s2 = '$%s$'%(latex(kq2))
            da_s3 = '$%s$'%(latex(kq3))
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_1 = [da_d,da_s1,da_s2,da_s3]
            random.shuffle(list_1)
            # Nội dung lời giải
            loigiai=('Số tiền thuê xe từ thứ Hai đến thứ Sáu là $%sx+5 \\cdot %s$ (nghìn đồng). \\\\ \n'
                    'Số tiền thuê xe trong hai ngày cuối tuần là $%sy+2 \\cdot %s$ (nghìn đồng). \\\\ \n'
                    'Suy ra, tổng số tiền phải trả là $(%sx+5 \\cdot %s)+(%sy+2 \\cdot %s)=%s$. \\\\ \n'
                    'Theo bài toán ta có bất phương trình $%s \\le %s \\, 000 \\Leftrightarrow %s$.'
                    %(latex(c),latex(a),
                    latex(d),latex(b),
                    latex(c),latex(a),latex(d),latex(b),latex(bt1),
                    latex(bt1),latex(e),latex(kq)
                        )    
                    )

                # Xuất câu hỏi
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-').replace('+0','').replace('-0','').replace('\\frac','\\dfrac')
            return content

