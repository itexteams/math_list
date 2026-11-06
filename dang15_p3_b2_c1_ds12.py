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


def bt_dang15_p3_b2_c1_ds12(self):
            lisdang=['1','2','3','4','5','6','7','8']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                a=randint(2,20)
                b=randint(7,20)
                p_1=b*100
                p_2=p_1-100
                v = a**3
                m=v*2*p_2
                r = round(((v*p_2)/p_1)**(1/3),1)
                h=v/(r**2)
                s = round(p_1*r**2+p_2*(2*a**3)/r,1)
                n=['nhà máy','công ty']
                ten=random.choice(n)
                number = Decimal(float(h))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một %s thiết kế một hình trụ bằng tôn không có nắp, có thể tích là $%s\\pi$ dm$^3$. Giá vật liệu làm mặt đáy và thành xung quanh lần lượt là %s đồng/dm$^2$ và %s đồng/dm$^2$. Hỏi bán chiều của hình trụ bằng bao nhiêu dm thì chi phí sản xuất thấp nhất? (làm tròn kết quả đến hàng phần chục). \n'
                                %(ten,latex(v),latex(p_1),latex(p_2))
                                )

                # Nội dung lời giải
                loigiai = (	'Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                            'Diện tích đáy của hình trụ là $S_1=\\pi r^2$.\\\\ \n' 
                            'Chi phí làm mặt đáy của hình trụ là $P_1=%s\\pi r^2$ đồng.\\\\ \n'
                            'Diện tích xung quanh của hình trụ là $S_2=2\\pi rh$.\\\\ \n'
                            'Chi phí làm thành xung quanh của hình trụ là $P_2=2\\pi rh\\cdot %s=%s\\pi rh$ đồng.\\\\ \n'
                            'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'
                            'Suy ra\\\\ \n' 
                            '\\hspace*{1cm} $P_2=%s\\pi r\\dfrac{%s}{r^2}=\\dfrac{%s\\pi}{r}$ đồng.\\\\ \n'
                            'Tổng chi phí sản xuất hình trụ là $P=P_1+P_2=%s\\pi r^2+\\dfrac{%s\\pi}{r}$ đồng.\\\\ \n'
                            'Ta có\\\\ \n'
                            '\\hspace*{1cm} $P\'=%s\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'
                            '\\hspace*{1cm} $P\'=0 \\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow %s\\pi r- \\dfrac{%s\\pi}{r^2} =0\\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow %sr^3 -%s=0\\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow r^3=\\dfrac{%s}{%s} \\Leftrightarrow r=\\sqrt[3]{\\dfrac{%s}{%s}} \\Leftrightarrow r \\approx %s$.\\\\ \n'
                            'Bảng biến thiên\\\\ \n' 
                            '\\begin{center}\n'
                                '\\begin{tikzpicture}\n'
                                    '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                                    '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                                    '{$r$ /0.6, $P\'$ /0.8, $P$ /2.5}\n'
                                    '{$0$,$%s$,$+\\infty$}\n'
                                    '\\tkzTabLine{d,-,$0$,+}\n'
                                    '\\tkzTabVar{D+/$+\\infty$,-/$%s$,+/$+\\infty$}\n'
                                '\\end{tikzpicture}\n'
                            '\\end{center}\n'
                            'Từ bảng biến thiên ta thấy $\\min P=%s$ đồng khi $r \\approx %s$ dm.\\\\ \n'
                            'Vậy $h = \\dfrac{V}{r^2}=\\dfrac{%s}{(%s)^2} \\approx %s$ dm.\\\\ \n'

                            %( latex(p_1),
                                latex(p_2),latex(2*p_2),   
                                latex(v),latex(v),
                                latex(2*p_2),latex(v),latex(2*p_2*v),
                                latex(p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),latex(2*p_2*v),latex(2*p_1),latex(2*p_2*v),latex(2*p_1),latex(r),
                                latex(r), latex(s),latex(s),latex(r),
                                latex(v), latex(r), latex(kq),

                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='2':
                # Khai báo biến
                a=randint(2,20)
                b=randint(7,20)
                p_1=b*100
                p_2=p_1-100
                v = a**3
                m=v*2*p_2
                r = round(((v*p_2)/p_1)**(1/3),1)
                h= nsimplify(v/r**2)
                s = round(p_1*r**2+p_2*(2*a**3)/r,1)
                n=['nhà máy','công ty']
                ten=random.choice(n)
                zz=r
                number = Decimal(float(zz))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một %s thiết kế một hình trụ bằng tôn không có nắp, có thể tích là $%s\\pi$ dm$^3$. Giá vật liệu làm mặt đáy và thành xung quanh lần lượt là %s đồng/dm$^2$ và %s đồng/dm$^2$. Hỏi bán kính đáy của hình trụ bằng bao nhiêu dm thì chi phí sản xuất thấp nhất? (làm tròn kết quả đến hàng phần chục).  \n'
                                %(ten,latex(v),latex(p_1),latex(p_2))
                                )

                # Nội dung lời giải
                loigiai = (	'Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                            'Diện tích đáy của hình trụ là $S_1=\\pi r^2$.\\\\ \n' 
                            'Chi phí làm mặt đáy của hình trụ là $P_1=%s\\pi r^2$ đồng.\\\\ \n'
                            'Diện tích xung quanh của hình trụ là $S_2=2\\pi rh$.\\\\ \n'
                            'Chi phí làm thành xung quanh của hình trụ là $P_2=2\\pi rh\\cdot %s=%s\\pi rh$ đồng.\\\\ \n'
                            'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'
                            'Suy ra\\\\ \n' 
                            '\\hspace*{1cm} $P_2=%s\\pi r\\dfrac{%s}{r^2}=\\dfrac{%s\\pi}{r}$ đồng.\\\\ \n'
                            'Tổng chi phí sản xuất hình trụ là $P=P_1+P_2=%s\\pi r^2+\\dfrac{%s\\pi}{r}$ đồng.\\\\ \n'
                            'Ta có\\\\ \n'
                            '\\hspace*{1cm} $P\'=%s\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'
                            '\\hspace*{1cm} $P\'=0 \\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow %s\\pi r- \\dfrac{%s\\pi}{r^2} =0\\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow %sr^3 -%s=0\\\\ \n'
                            '\\hspace*{1cm} \\Leftrightarrow r^3=\\dfrac{%s}{%s} \\Leftrightarrow r=\\sqrt[3]{\\dfrac{%s}{%s}} \\Leftrightarrow r \\approx %s$.\\\\ \n'
                            'Bảng biến thiên\\\\ \n' 
                            '\\begin{center}\n'
                                '\\begin{tikzpicture}\n'
                                    '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                                    '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                                    '{$r$ /0.6, $P\'$ /0.8, $P$ /2.5}\n'
                                    '{$0$,$%s$,$+\\infty$}\n'
                                    '\\tkzTabLine{d,-,$0$,+}\n'
                                    '\\tkzTabVar{D+/$+\\infty$,-/$%s$,+/$+\\infty$}\n'
                                '\\end{tikzpicture}\n'
                            '\\end{center}\n'
                            'Từ bảng biến thiên ta thấy $\\min P=%s$ đồng khi $r \\approx %s$ dm.\\\\ \n'
                            'Vậy $ r \\approx %s$ dm.\\\\ \n'

                            %( latex(p_1),
                                latex(p_2),latex(2*p_2),   
                                latex(v),latex(v),
                                latex(2*p_2),latex(v),latex(2*p_2*v),
                                latex(p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),
                                latex(2*p_1),latex(2*p_2*v),latex(2*p_2*v),latex(2*p_1),latex(2*p_2*v),latex(2*p_1),latex(r),
                                latex(r), latex(s),latex(s),latex(r),latex(kq),

                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='3':
                # Khai báo biến
                a=randint(2,20)
                v = a**3
                r=a
                h=a
                s = nsimplify(r**2+(2*a**3)/r)
                n=['nhà máy','công ty']
                ten=random.choice(n)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một %s thiết kế một hình trụ bằng tôn không có nắp, có thể tích là $%s\\pi$ dm$^3$. Giả sử diện tích bề mặt của hình trụ bằng $x\\pi$ dm$^2$. Hỏi giá trị của $x$ bằng bao nhiêu thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(ten,latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_1=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_2=2\\pi rh$.\\\\ \n'
                'Diện tích phần vật liệu làm hình trụ là $S=S_1+S_2 = \\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S=\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích $S$ nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'=2\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'=0 \\Leftrightarrow 2\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'$ /0.8, $S$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Từ bảng biến thiên ta thấy $\\min S=%s\\pi$ dm$^2$.\\\\ \n'
                'Vậy giá trị của $x$ là $%s$.\\\\ \n'   


                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),
                            latex(s), latex(s)
                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(s))

            if dang=='4':
                # Khai báo biến
                a=randint(2,20)
                v = a**3
                r=a
                h=a
                s = nsimplify(r**2+(2*a**3)/r)
                n=['nhà máy','công ty']
                ten=random.choice(n)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một %s thiết kế một hình trụ bằng tôn không có nắp, có thể tích là $%s\\pi$ dm$^3$. Hỏi chiều cao của hình trụ bằng bao nhiêu dm thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(ten,latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_1=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_2=2\\pi rh$.\\\\ \n'
                'Diện tích phần vật liệu làm hình trụ là $S=S_1+S_2 = \\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S=\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích $S$ nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'=2\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'=0 \\Leftrightarrow 2\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'$ /0.8, $S$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Với $r=%s$ dm thì hình trụ làm ra tốn ít vật liệu nhất.\\\\ \n'
                'Vậy chiều cao của hình trụ $h=\\dfrac{%s}{r^2}=\\dfrac{%s}{%s^2}=%s$ dm .\\\\ \n'    


                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),latex(a),
                            latex(v), latex(v),latex(a),latex(a),
                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            if dang=='5':
                # Khai báo biến
                a=randint(2,20)
                v = a**3
                r=a
                h=a
                s = nsimplify(r**2+(2*a**3)/r)
                n=['nhà máy','công ty']
                ten=random.choice(n)

                # Nội dung câu hỏi
                noidungcauhoi = ('Một %s thiết kế một hình trụ bằng tôn không có nắp, có thể tích là $%s\\pi$ dm$^3$. Hỏi bán kính đáy của hình trụ bằng bao nhiêu dm thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(ten,latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_1=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_2=2\\pi rh$.\\\\ \n'
                'Diện tích phần vật liệu làm hình trụ là $S=S_1+S_2 = \\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S=\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích $S$ nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'=2\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'=0 \\Leftrightarrow 2\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'$ /0.8, $S$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Vậy với $r=%s$ dm thì hình trụ làm ra tốn ít vật liệu nhất.\\\\ \n'


                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),latex(a),

                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(a)

            if dang=='6':
                # Khai báo biến
                a=randint(2,20)
                v = 2*a**3
                r=a
                h=2*a
                s = nsimplify(2*r**2+(4*a**3)/r)
                # Nội dung câu hỏi
                noidungcauhoi = ('Một nhà máy thiết kế một hình trụ bằng tôn có nắp, có thể tích là $%s\\pi$ dm$^3$. Giả sử diện tích bề mặt của hình trụ bằng $x\\pi$ dm$^2$. Hỏi giá trị của $x$ bằng bao nhiêu thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_{\\text{đ}}=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_{\\text{xq}}=2\\pi rh$.\\\\ \n'
                'Diện tích toàn phần của hình trụ là $S_{\\text{tp}}=2S_{\\text{đ}}+S_{\\text{xq}} = 2\\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S_{\\text{tp}}=2\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=2\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích toàn phần nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'_{\\text{tp}}=4\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'_{\\text{tp}}=0 \\Leftrightarrow 4\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'_{tp}$ /0.8, $S_{tp}$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Từ bảng biến thiên ta thấy $\\min S_{tp}=%s\\pi$ dm$^2$.\\\\ \n'
                'Vậy giá trị của $x$ là $%s$ .\\\\ \n'    

                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),
                            latex(s),latex(s),
                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(s)

            if dang=='7':
                # Khai báo biến
                a=randint(2,20)
                v = 2*a**3
                r=a
                h=2*a
                s = nsimplify(2*r**2+(4*a**3)/r)
                # Nội dung câu hỏi
                noidungcauhoi = ('Một nhà máy thiết kế một hình trụ bằng tôn có nắp, có thể tích là $%s\\pi$ dm$^3$. Hỏi chiều cao của hình trụ bằng bao nhiêu dm thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_{\\text{đ}}=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_{\\text{xq}}=2\\pi rh$.\\\\ \n'
                'Diện tích toàn phần của hình trụ là $S_{\\text{tp}}=2S_{\\text{đ}}+S_{\\text{xq}} = 2\\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S_{\\text{tp}}=2\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=2\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích toàn phần nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'_{\\text{tp}}=4\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'_{\\text{tp}}=0 \\Leftrightarrow 4\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'_{tp}$ /0.8, $S_{tp}$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Với $r=%s$ $dm$ thì hình trụ làm ra tốn ít vật liệu nhất.\\\\ \n'
                'Vậy chiều cao của hình trụ $h=\\dfrac{%s}{r^2}=\\dfrac{%s}{%s^2}=%s$ dm .\\\\ \n'    

                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),latex(a),
                            latex(v), latex(v),latex(a),latex(2*a),
                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(2*a)

            if dang=='8':
                # Khai báo biến
                a=randint(2,20)
                v = 2*a**3
                r=a
                h=2*a
                s = nsimplify(2*r**2+(4*a**3)/r)
                # Nội dung câu hỏi
                noidungcauhoi = ('Một nhà máy thiết kế một hình trụ bằng tôn có nắp, có thể tích là $%s\\pi$ dm$^3$. Hỏi chiều cao của hình trụ bằng bao nhiêu dm thì hình trụ được làm ra tốn ít vật liệu nhất? \n'
                                %(latex(v)))

                # Nội dung lời giải
                loigiai = ('Gọi bán kính và chiều cao của hình trụ lần lượt là $r,h$ $(r>0,h>0)$.\\\\ \n'
                        'Diện tích một đáy của hình trụ là $S_{\\text{đ}}=\\pi r^2$.\\\\ \n'
                'Diện tích xung quanh của hình trụ là $S_{\\text{xq}}=2\\pi rh$.\\\\ \n'
                'Diện tích toàn phần của hình trụ là $S_{\\text{tp}}=2S_{\\text{đ}}+S_{\\text{xq}} = 2\\pi r^2+2\\pi rh$.\\\\ \n'
                'Theo bài ta có thể tích của hình trụ $V=\\pi r^2h=%s\\pi \\Rightarrow h=\\dfrac{%s}{r^2}$.\\\\ \n'#
                'Suy ra\\\\ \n'
                '\\hspace*{1cm} $S_{\\text{tp}}=2\\pi r^2+2\\pi r\\cdot \\left( \\dfrac{%s}{r^2} \\right)=2\\pi r^2+ \\dfrac{%s\\pi}{r}$.\\\\ \n'##
                'Để tốn ít vật liệu nhất thì diện tích toàn phần nhỏ nhất.\\\\ \n'
                'Ta có\\\\ \n'
                '\\hspace*{1cm} $S\'_{\\text{tp}}=4\\pi r- \\dfrac{%s\\pi}{r^2}$.\\\\ \n'###
                '\\hspace*{1cm} $S\'_{\\text{tp}}=0 \\Leftrightarrow 4\\pi r- \\dfrac{%s\\pi}{r^2} =0 \\Leftrightarrow r^3 -%s=0 \\Leftrightarrow r^3=%s \\Leftrightarrow r=\\sqrt[3]{%s} \\Leftrightarrow r=%s$.\\\\ \n'
                'Bảng biến thiên\\\\ \n'
                '\\begin{center}\n'
                    '\\begin{tikzpicture}\n'
                        '\\tikzset{double style/.append style={double distance=1.5pt}}\n'
                        '\\tkzTabInit[nocadre=false,lgt=1.2,espcl=2.5,deltacl=0.6]\n'
                        '{$r$ /0.6, $S\'_{tp}$ /0.8, $S_{tp}$ /2.5}\n'
                        '{$0$,$%s$,$+\\infty$}\n' #5
                        '\\tkzTabLine{d,-,$0$,+}\n'
                        '\\tkzTabVar{D+/$+\\infty$,-/$%s\\pi$,+/$+\\infty$}\n'#6
                    '\\end{tikzpicture}\n'
                '\\end{center}\n'
                'Vậy với $r=%s$ dm và $h=%s$ thì hình trụ làm ra tốn ít vật liệu nhất.\\\\ \n'


                            %(latex(v),latex(v),#
                            latex(v),latex(2*v),##
                            latex(2*v),###
                            latex(2*v), latex(a**3), latex(a**3), latex(a**3),#4
                            latex(a),#5
                            latex(a), latex(s),latex(a),latex(2*a)

                                )
                            )
                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(2*a)

                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                    '\\loigiai{ \n'
                    +str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

