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


def bt_dang22_p3_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                a=randint(3,6)
                k=randint(4,9)
                chi_phi=k*100
                tien1=chi_phi/1000
                tien=str(tien1).replace('.', ',')
                s=expand((a-2*x)**2+2*x**2)
                dh=diff(s,x)
                pt=Eq(dh,0)
                nghiem=solve(pt,x)
                x0=nghiem[0]
                s0=(a-2*0)**2+2*0**2
                sx0=(a-2*x0)**2+2*x0**2
                sa=(a-2*a)**2+2*a**2

                kqz=sx0*tien1


                h1=sx0*tien1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                kq1=str(kq).replace('.', ',')

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Cho hình vuông $ABCD$ có cạnh bằng $%s$ m, chính giữa có một hình vuông đồng tâm với hình vuông $ABCD$ (xem hình vẽ). Biết rằng bốn tam giác tô màu trên hình là bốn tam giác cân. Người ta cần sơn cho hình vuông ở giữa và bốn tam giác cân trên, chi phí là $%s$ nghìn đồng trên một mét vuông. Hỏi cần bỏ ra ít nhất bao nhiêu triệu đồng? (kết quả làm tròn đến hàng phần chục).}
                                {\\begin{tikzpicture}[scale=1]
                \\draw[thick] (0,0) rectangle (4,4);
            \\fill[orange] (1.3,2) -- (2,2.7) -- (2.7,2) -- (2,1.3) -- cycle;
            \\draw[thick] (1.3,2) -- (2,2.7) -- (2.7,2) -- (2,1.3) -- cycle;
            \\fill[green] (0.7,4) -- (3.3,4) -- (2,2.7) -- cycle;
            \\draw[thick] (0.7,4) -- (3.3,4) -- (2,2.7) -- cycle;
            \\fill[blue] (0.7,0) -- (3.3,0) -- (2,1.3) -- cycle;
            \\draw[thick] (0.7,0) -- (3.3,0) -- (2,1.3) -- cycle;
            \\fill[red] (0,0.7) -- (0,3.3) -- (1.3,2) -- cycle;
            \\draw[thick] (0,0.7) -- (0,3.3) -- (1.3,2) -- cycle;
            \\fill[yellow] (4,0.7) -- (4,3.3) -- (2.7,2) -- cycle;
            \\draw[thick] (4,0.7) -- (4,3.3) -- (2.7,2) -- cycle;
            \\node[below left] at (0,0) { $D$};
            \\node[below right] at (4,0) { $C$};
            \\node[above right] at (4,4) { $B$};
            \\node[above left] at (0,4) { $A$};
            \\end{tikzpicture}}'''
                                %(latex(a),latex(chi_phi)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[scale=1]
                \\draw[thick] (0,0) rectangle (4,4);
                \\fill[orange] (1.3,2) -- (2,2.7) -- (2.7,2) -- (2,1.3) -- cycle;
                \\draw[thick] (1.3,2) -- (2,2.7) -- (2.7,2) -- (2,1.3) -- cycle;
                \\fill[green] (0.7,4) -- (3.3,4) -- (2,2.7) -- cycle;
                \\draw[thick] (0.7,4) -- (3.3,4) -- (2,2.7) -- cycle;
                \\fill[blue] (0.7,0) -- (3.3,0) -- (2,1.3) -- cycle;
                \\draw[thick] (0.7,0) -- (3.3,0) -- (2,1.3) -- cycle;
                \\fill[red] (0,0.7) -- (0,3.3) -- (1.3,2) -- cycle;
                \\draw[thick] (0,0.7) -- (0,3.3) -- (1.3,2) -- cycle;
                \\fill[yellow] (4,0.7) -- (4,3.3) -- (2.7,2) -- cycle;
                \\draw[thick] (4,0.7) -- (4,3.3) -- (2.7,2) -- cycle;
                    \\node[below left] at (0,0) { $D$};
                    \\node[below right] at (4,0) { $C$};
                    \\node[above right] at (4,4) { $B$};
                    \\node[above left] at (0,4) { $A$};
                    \\node[above left] at (1,4) { $M$};
                    \\node[below left] at (0,3) { $N$};
                    \\node[above left] at (3,4) { $E$};
                    \\node[above] at (1.3,2) { $P$};
                    \\node[left] at (2,2.7) { $Q$};
                    \\node[above left] at (0.5,4) { $x$};
                    \\node[above left] at (2.5,4) { $%s-2x$};
                \\end{tikzpicture}
            \\end{center}
                        Đặt $AM=x$ với $(0 <x <%s) \\Rightarrow ME=%s-2x, MN=x\\sqrt{2}$ và $2MQ^2=ME^2=(%s-2x)^2$. \\\\
                        Gọi $S$ là tổng diện tích của hình vuông ở giữa và bốn tam giác cân nhỏ, ta có \\\\
                            \\hspace*{1cm} $S=4 \\cdot \\frac{MQ^2}{2}+PQ^2=2MQ^2+MN^2=(%s-2x)^2+(x\\sqrt{2})^2=%s$. \\\\
                                \\hspace*{1cm} $S'=%s$. \\\\
                                    \\hspace*{1cm} $S'=0 \\Leftrightarrow %s=0 \\Leftrightarrow x=%s$. \\\\
                            \\hspace*{1cm} Bảng biến thiên \\\\
                            \\hspace*{1cm} \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$S'$/0.7,$S$/2.1}
            {$0$,$%s$,$%s$}
            \\tkzTabLine{,-,0,+}
            \\tkzTabVar{+/$%s$,-/$%s$,+/$%s$}
            \\end{tikzpicture} \\\\
            Suy ra $S_{min}=%s$. Vậy số tiền tối thiểu cần bỏ ra là $T=%s \\cdot %s=%s$ triệu đồng.'''
                        %(latex(a),latex(a),latex(a),latex(a),latex(a),latex(s),
                            latex(dh),
                            latex(dh),latex(x0),
                            latex(x0),latex(a),
                            latex(s0),latex(sx0),latex(sa),
                            latex(sx0),
                            latex(sx0),latex(tien),latex(kq1)
                        ))

                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq1))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\left[', '').replace('\\right]', '')
            return content

