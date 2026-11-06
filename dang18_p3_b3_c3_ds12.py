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


def bt_dang18_p3_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                lis1=[400,500,600,700,800]
                dai=random.choice(lis1)
                nhip=10
                kc_nhip=Rational(dai-100,10)
                rong=5
                day=randint(20,30)
                cao=2

                a1=-rong-Rational(kc_nhip,2)
                a2=rong+Rational(kc_nhip,2)
                a3=cao

                x=symbols('x')
                a=-Rational(cao,a1**2)
                b=0
                c=cao
                f1=a*x**2+b*x+c

                a1z=-rong-Rational(kc_nhip,2)+Rational(day,100)
                a2z=rong+Rational(kc_nhip,2)-Rational(day,100)
                a3z=cao-Rational(day,100)
                az=-Rational(cao-Rational(day,100),a1z**2)
                bz=0
                cz=cao-Rational(day,100)

                f2=az*x**2+bz*x+cz

                s1=integrate(f1, (x, a1, a2))
                s2=integrate(f2, (x, a1z, a2z))
                s=s1-s2

                v=Rational(dai,kc_nhip+2*rong)*(s*day/100)

                h1=v
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Thành phố định xây cây cầu bắc ngang con sông dài $%s$ m, biết rằng người ta định xây cầu có $%s$ nhịp cầu hình dạng parabol, mỗi nhịp cách nhau $%s$ m, biết hai bên đầu cầu và giữa mỗi nhịp nối người ta xây một chân trụ rộng $%s$ m. Bề dày nhịp cầu không đổi là $%s$ cm. Biết một nhịp cầu như hình vē. Hỏi lượng bê tông (làm tròn kết quả đến hàng đơn vị) để xây các nhịp cầu là bao nhiêu mét khối (bỏ qua diện tích cốt sắt trong mỗi nhịp cầu)?}
                                {
                                    \\scalebox{0.7}{ 
            \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
            \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-0.19620124345137172,-1.5663876814784357) rectangle (8.233706907304935,2.2882840123528565);
                    \\fill[line width=1.pt,fill=black,pattern=north east lines,pattern color=black] (0.,0.) -- (0.,-1.) -- (2.,-1.) -- (2.,0.) -- cycle;
                    \\fill[line width=1.pt,fill=black,pattern=north east lines,pattern color=black] (6.,0.) -- (8.,0.) -- (8.,-1.) -- (6.,-1.) -- cycle;
                    \\draw [line width=1.pt] (0.,0.)-- (0.,-1.);
                    \\draw [line width=1.pt] (0.,-1.)-- (2.,-1.);
                    \\draw [line width=1.pt] (2.,-1.)-- (2.,0.);
                    \\draw [line width=1.pt] (2.,0.)-- (0.,0.);
                    \\draw [line width=1.pt] (6.,0.)-- (8.,0.);
                    \\draw [line width=1.pt] (8.,0.)-- (8.,-1.);
                    \\draw [line width=1.pt] (8.,-1.)-- (6.,-1.);
                    \\draw [line width=1.pt] (6.,-1.)-- (6.,0.);
                    \\draw [shift={(4.,-3.)},line width=1.pt]  plot[domain=0.6435011087932844:2.498091544796509,variable=\\t]({1.*5.*cos(\\t r)+0.*5.*sin(\\t r)},{0.*5.*cos(\\t r)+1.*5.*sin(\\t r)});
                    \\draw [shift={(4.,-3.099371862508574)},line width=1.pt]  plot[domain=0.8016888690509228:2.3399037845388704,variable=\\t]({1.*4.313479563196036*cos(\\t r)+0.*4.313479563196036*sin(\\t r)},{0.*4.313479563196036*cos(\\t r)+1.*4.313479563196036*sin(\\t r)});
                    \\draw [line width=1.pt,color=ffqqqq] (4.,2.)-- (2.996633017225687,1.0957873287484436);
                    \\draw [line width=1.pt,color=ffqqqq] (4.,2.)-- (5.006842513573009,1.0949545548046813);
                    \\draw [line width=1.pt,color=ffqqqq] (2.996633017225687,1.0957873287484436)-- (2.0083372218194118,1.5862053353518721);
                    \\draw [line width=1.pt,color=ffqqqq] (5.006842513573009,1.0949545548046813)-- (5.993033554328246,1.5856098014682543);
                    \\draw [line width=1.pt,color=ffqqqq] (2.0083372218194118,1.5862053353518721)-- (1.4980983927281244,0.4144002259513866);
                    \\draw [line width=1.pt,color=ffqqqq] (1.4980983927281244,0.4144002259513866)-- (0.,0.);
                    \\draw [line width=1.pt,color=ffqqqq] (5.993033554328246,1.5856098014682543)-- (6.509198732651747,0.4091930381550477);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (8.,0.);
                    \\draw [line width=1.pt] (4.,2.)-- (4.013092694067969,1.214087830530403);
                    \\draw [line width=1.pt,color=ffqqqq] (3.0116254955863684,1.9013381681970394)-- (2.996633017225687,1.0957873287484436);
                    \\draw [line width=1.pt,color=ffqqqq] (5.005662064042819,1.897820312439518)-- (5.006842513573009,1.0949545548046813);
                    \\draw [line width=1.pt,color=ffqqqq] (2.0083372218194118,1.5862053353518721)-- (2.0023530746591556,0.7236521635454256);
                    \\draw [line width=1.pt,color=ffqqqq] (1.4980983927281244,0.4144002259513866)-- (0.4372237405942281,0.5080800055606791);
                    \\draw [line width=1.pt] (1.4980983927281244,0.4144002259513866)-- (1.,1.);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (7.569757675872455,0.5009755976798367);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (7.,1.);
                    \\draw [line width=1.pt,color=ffqqqq] (5.993033554328246,1.5856098014682543)-- (6.00820622417924,0.7181160160940054);
                    \\draw [->,line width=1.pt] (0.9441099835803943,-1.1326496687424281) -- (2.0074676922235137,-1.1326496687424281);
                    \\draw [->,line width=1.pt] (0.9441099835803943,-1.1326496687424281) -- (-0.014311109078206541,-1.1256538943434604);
                    \\draw [->,line width=1.pt] (7.02343793628349,-1.1046665711465566) -- (8.01683790093693,-1.1046665711465566);
                    \\draw [->,line width=1.pt] (7.02343793628349,-1.1046665711465566) -- (6.0090506484331465,-1.1046665711465566);
                    \\draw [->,line width=1.pt] (4.013092694067969,1.214087830530403) -- (4.,2.);
                    \\draw [->,line width=1.pt] (4.013092694067969,1.214087830530403) -- (4.057229591121105,-0.020321539306538128);
                    \\draw [->,line width=1.pt] (5.022646458178674,0.) -- (6.,0.);
                    \\draw [->,line width=1.pt] (5.022646458178674,0.) -- (4.057229591121105,-0.020321539306538124);
                    \\draw [->,line width=1.pt] (2.993871882477986,0.) -- (4.057229591121105,-0.020321539306538124);
                    \\draw [->,line width=1.pt] (2.993871882477986,0.) -- (2.,0.);
                    \\draw (0.7762113980051649,-1.0766834735506854) node[anchor=north west] {$%s$m};
                    \\draw (6.862535125107229,-1.0556961503537816) node[anchor=north west] {$%s$m};
                    \\draw (2.8399648457006923,0.0496362046831405) node[anchor=north west] {$%s$m};
                    \\draw (4.896722518997252,0.04264043028417264) node[anchor=north west] {$%s$m};
                    \\draw (4.036242267924202,1.0710192669324483) node[anchor=north west] {$%s$m};
                    \\draw [->,line width=1.pt] (1.2467842399766853,0.7098629562372702) -- (1.,1.);
                    \\draw [->,line width=1.pt] (1.2467842399766853,0.7098629562372702) -- (1.4980983927281244,0.4144002259513866);
                    \\draw (0,1.5) node[anchor=north west] {$%s$cm};
            \\end{tikzpicture} }}
            '''
                                %(latex(dai),latex(nhip),latex(kc_nhip),latex(rong),latex(day),
                                latex(rong),latex(rong),latex(Rational(kc_nhip,2)),latex(Rational(kc_nhip,2)),latex(cao),latex(day)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-0.6579223537832525,-1.5593919070794677) rectangle (8.611478724849201,2.6240811835033138);
                    \\fill[line width=1.pt,fill=black,pattern=north east lines,pattern color=black] (0.,0.) -- (0.,-1.) -- (2.,-1.) -- (2.,0.) -- cycle;
                    \\fill[line width=1.pt,fill=black,pattern=north east lines,pattern color=black] (6.,0.) -- (8.,0.) -- (8.,-1.) -- (6.,-1.) -- cycle;
                    \\draw [line width=1.pt] (0.,0.)-- (0.,-1.);
                    \\draw [line width=1.pt] (0.,-1.)-- (2.,-1.);
                    \\draw [line width=1.pt] (2.,-1.)-- (2.,0.);
                    \\draw [line width=1.pt] (2.,0.)-- (0.,0.);
                    \\draw [line width=1.pt] (6.,0.)-- (8.,0.);
                    \\draw [line width=1.pt] (8.,0.)-- (8.,-1.);
                    \\draw [line width=1.pt] (8.,-1.)-- (6.,-1.);
                    \\draw [line width=1.pt] (6.,-1.)-- (6.,0.);
                    \\draw [shift={(4.,-3.)},line width=1.pt]  plot[domain=0.6435011087932844:2.498091544796509,variable=\\t]({1.*5.*cos(\\t r)+0.*5.*sin(\\t r)},{0.*5.*cos(\\t r)+1.*5.*sin(\\t r)});
                    \\draw [shift={(4.,-3.099371862508574)},line width=1.pt]  plot[domain=0.8016888690509228:2.3399037845388704,variable=\\t]({1.*4.313479563196036*cos(\\t r)+0.*4.313479563196036*sin(\\t r)},{0.*4.313479563196036*cos(\\t r)+1.*4.313479563196036*sin(\\t r)});
                    \\draw [line width=1.pt,color=ffqqqq] (4.,2.)-- (2.996633017225687,1.0957873287484436);
                    \\draw [line width=1.pt,color=ffqqqq] (4.,2.)-- (5.006842513573009,1.0949545548046813);
                    \\draw [line width=1.pt,color=ffqqqq] (2.996633017225687,1.0957873287484436)-- (2.0083372218194118,1.5862053353518721);
                    \\draw [line width=1.pt,color=ffqqqq] (5.006842513573009,1.0949545548046813)-- (5.993033554328246,1.5856098014682543);
                    \\draw [line width=1.pt,color=ffqqqq] (2.0083372218194118,1.5862053353518721)-- (1.4980983927281244,0.4144002259513866);
                    \\draw [line width=1.pt,color=ffqqqq] (1.4980983927281244,0.4144002259513866)-- (0.,0.);
                    \\draw [line width=1.pt,color=ffqqqq] (5.993033554328246,1.5856098014682543)-- (6.509198732651747,0.4091930381550477);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (8.,0.);
                    \\draw [line width=1.pt] (4.,2.)-- (4.013092694067969,1.214087830530403);
                    \\draw [line width=1.pt,color=ffqqqq] (3.0116254955863684,1.9013381681970394)-- (2.996633017225687,1.0957873287484436);
                    \\draw [line width=1.pt,color=ffqqqq] (5.005662064042819,1.897820312439518)-- (5.006842513573009,1.0949545548046813);
                    \\draw [line width=1.pt,color=ffqqqq] (2.0083372218194118,1.5862053353518721)-- (2.0023530746591556,0.7236521635454256);
                    \\draw [line width=1.pt,color=ffqqqq] (1.4980983927281244,0.4144002259513866)-- (0.4372237405942281,0.5080800055606791);
                    \\draw [line width=1.pt] (1.4980983927281244,0.4144002259513866)-- (1.,1.);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (7.569757675872455,0.5009755976798367);
                    \\draw [line width=1.pt,color=ffqqqq] (6.509198732651747,0.4091930381550477)-- (7.,1.);
                    \\draw [line width=1.pt,color=ffqqqq] (5.993033554328246,1.5856098014682543)-- (6.00820622417924,0.7181160160940054);
                    \\draw [->,line width=1.pt] (0.9441099835803943,-1.1326496687424281) -- (2.0074676922235137,-1.1326496687424281);
                    \\draw [->,line width=1.pt] (0.9441099835803943,-1.1326496687424281) -- (-0.014311109078206541,-1.1256538943434604);
                    \\draw [->,line width=1.pt] (7.02343793628349,-1.1046665711465566) -- (8.01683790093693,-1.1046665711465566);
                    \\draw [->,line width=1.pt] (7.02343793628349,-1.1046665711465566) -- (6.0090506484331465,-1.1046665711465566);
                    \\draw [->,line width=1.pt] (4.013092694067969,1.214087830530403) -- (4.,2.);
                    \\draw [->,line width=1.pt] (4.013092694067969,1.214087830530403) -- (4.,0.);
                    \\draw [->,line width=1.pt] (5.022646458178674,0.) -- (6.,0.);
                    \\draw [->,line width=1.pt] (5.022646458178674,0.) -- (4.,0.);
                    \\draw [->,line width=1.pt] (2.993871882477986,0.) -- (4.,0.);
                    \\draw [->,line width=1.pt] (2.993871882477986,0.) -- (2.,0.);
                    \\draw (0.7762113980051649,-1.0766834735506854) node[anchor=north west] {$%s$m};
                    \\draw (6.862535125107229,-1.0556961503537816) node[anchor=north west] {$%s$m};
                    \\draw (2.5,0.0496362046831405) node[anchor=north west] {$%s$m};
                    \\draw (4.72,0.04264043028417264) node[anchor=north west] {$%s$m};
                    \\draw (4.036242267924202,1.0710192669324483) node[anchor=north west] {$%s$m};
                    \\draw [->,line width=1.pt] (1.2467842399766853,0.7098629562372702) -- (1.,1.);
                    \\draw [->,line width=1.pt] (1.2467842399766853,0.7098629562372702) -- (1.4980983927281244,0.4144002259513866);
                    \\draw (0,1.385829114886002) node[anchor=north west] {$%s$cm};
                    \\draw [->,line width=1.pt] (-0.5,0.) -- (8.5,0.);
                    \\draw [->,line width=1.pt] (4.,-0.5) -- (4.,2.5);
                    \\draw (3.5,0.035644655885204775) node[anchor=north west] {$O$};
                    \\draw (8.28267732809771,0.0496362046831405) node[anchor=north west] {$x$};
                    \\draw (3.9,2.5261403419177637) node[anchor=north west] {$y$};
                \\end{tikzpicture}
            \\end{center}
                        Chọn hệ trục $(Oxy)$ như hình vẽ với gốc $O(0;0)$. \\\\
                        Gọi parabol trên có phương trình $(P_1):y_1=ax^2+bx+c$. \\\\
                        Ta thấy $(P_1)$ đi qua các điểm $(-%s;0); (%s;0)$ và $(0;%s)$. \\\\
                        Nên ta có hệ phương trình $\\heva{&%s a+%s b+c=0\\\\&%s a+%s b+c=0\\\\&c=%s} \\Leftrightarrow \\heva{& a=%s \\\\& b=0\\\\&c=%s}$. \\\\
                        Suy ra $y_1=%s$. \\\\
                        Gọi parabol dưới có phương trình $(P_2):y_2=ax^2+bx+c$. \\\\
                        Ta thấy $(P_2)$ đi qua các điểm $\\left(-%s;0\\right); \\left(%s;0\\right)$ và $\\left(0;%s\\right)$. \\\\
                        Nên ta có hệ phương trình $\\heva{&%s a+%s b+c=0\\\\&%s a+%s b+c=0\\\\&c=%s} \\Leftrightarrow \\heva{& a=%s \\\\& b=0\\\\&c=%s}$. \\\\
                        Suy ra $y_2=%s$. \\\\
                        Khi đó diện tích mỗi nhịp cầu là $S=\\int \\limits_{%s}^{%s} (y_1) \\text{d}x- \\int \\limits_{%s}^{%s} (y_2) \\text{d}x=%s$. \\\\
                            Vì chiều dày của nhịp cầu là $%s$ cm $=%s$ m nên thể tích mỗi nhịp cầu là \\\\
                                $V_1=%s \\cdot %s = %s$. \\\\
                                    Vậy thể tích bê tông để làm hết số nhịp cầu là $V=%s \\cdot V_1=%s \\approx %s$ m$^3$.''' 
                        %(
                            latex(rong),latex(rong),latex(Rational(kc_nhip,2)),latex(Rational(kc_nhip,2)),latex(cao),latex(day),
                            latex(rong+Rational(kc_nhip,2)),latex(rong+Rational(kc_nhip,2)),latex(cao),
                            latex(a1**2),latex(a1),latex(a2**2),latex(a2),latex(a3),
                            latex(a),latex(c),
                            latex(f1),
                            latex(-Rational(day,100)+rong+Rational(kc_nhip,2)),latex(-Rational(day,100)+rong+Rational(kc_nhip,2)),latex(cao-Rational(day,100)),
                            latex(a1z**2),latex(a1z),latex(a2z**2),latex(a2z),latex(a3z),
                            latex(az),latex(cz),
                            latex(f2),
                            latex(a1),latex(a2),latex(a1z),latex(a2z),latex(s),
                            latex(day),latex(day/100),
                            latex(day/100),latex(s),latex(s*day/100),
                            latex(Rational(dai,kc_nhip+2*rong)),latex(v),latex(kq)
                            ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content 

